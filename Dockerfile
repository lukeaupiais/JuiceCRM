# Base image for building the frontend
FROM node:18-alpine AS frontend-builder

# Set working directory
WORKDIR /app/frontend

# Copy frontend files
COPY ./frontend_setup_instructions.txt ./
RUN mkdir -p /app/frontend/app
RUN touch /app/frontend/app/package.json
RUN echo '{}' > /app/frontend/app/package.json


# Install frontend dependencies (replace with your actual frontend build steps)
# For example, if you have a package.json and source files:
# COPY frontend/package*.json ./
# RUN npm install
# COPY frontend/ ./
# RUN npm run build

# Base image for building the backend
FROM python:3.9-slim AS backend-builder

# Set working directory
WORKDIR /app/backend

# Copy backend files
COPY ./setup_instructions.txt ./

# Install backend dependencies (replace with your actual backend dependencies)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Final image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy built frontend from the frontend-builder stage
# Adjust the source path if your frontend build output is different
# COPY --from=frontend-builder /app/frontend/out ./
COPY --from=frontend-builder /app/frontend ./frontend


# Copy built backend from the backend-builder stage
COPY --from=backend-builder /app/backend ./

# Expose the port the application listens on (adjust as needed)
EXPOSE 8080

# Set environment variables (replace with your actual environment variables)
ENV DATABASE_URL=your_database_url
ENV API_KEY=your_api_key

# Command to run the application (replace with your actual startup command)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]