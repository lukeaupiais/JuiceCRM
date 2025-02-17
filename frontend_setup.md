# Frontend Environment Setup for MegaTEAM Juice Application

This document outlines the steps to set up the frontend development environment for the MegaTEAM Juice Application.

## Technologies Used

*   **Framework:** Next.js
*   **Styling:** Tailwind CSS
*   **Package Manager:** npm
*   **JavaScript Runtime:** Node.js

## Prerequisites

*   Node.js (version >= 16)
*   npm (version >= 8)

## Setup Instructions

1.  **Install Node.js and npm:**
    *   Download and install Node.js from [https://nodejs.org/](https://nodejs.org/). npm is included with Node.js.

2.  **Create Next.js Application:**
    *   Navigate to the project directory in the terminal: `cd C:\Users\aupia\Git\MegaTEAM\devteam\juice`
    *   Create a new Next.js application using `npx create-next-app frontend`

3.  **Install Tailwind CSS:**
    *   Navigate to the frontend directory: `cd frontend`
    *   Install Tailwind CSS and its peer dependencies:
        ```bash
        npm install -D tailwindcss postcss autoprefixer
        npx tailwindcss init -p
        ```

4.  **Configure Tailwind CSS:**
    *   Open `tailwind.config.js` and configure the `content` array to include your components and pages:
        ```javascript
        /** @type {import('tailwindcss').Config} */
        module.exports = {
          content: [
            './app/**/*.{js,ts,jsx,tsx,mdx}',
            './pages/**/*.{js,ts,jsx,tsx,mdx}',
            './components/**/*.{js,ts,jsx,tsx,mdx}',
            './src/**/*.{js,ts,jsx,tsx,mdx}',
          ],
          theme: {
            extend: {},
          },
          plugins: [],
        }
        ```

5.  **Add Tailwind Directives to Global CSS:**
    *   Open `styles/global.css` (or create it if it doesn't exist) and add the following Tailwind directives:
        ```css
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
        ```

6.  **Run the Development Server:**
    *   Start the Next.js development server:
        ```bash
        npm run dev
        ```
    *   Open your browser and navigate to `http://localhost:3000` to view the application.

## Verification

*   Verify that the Next.js application is running without errors.
*   Verify that Tailwind CSS styles are applied correctly.

## Troubleshooting

*   If you encounter any issues, refer to the Next.js and Tailwind CSS documentation for troubleshooting.

