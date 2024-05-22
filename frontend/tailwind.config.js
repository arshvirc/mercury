/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#3B82F6',  
          DEFAULT: '#A91D3A', 
          dark: '#1E3A8A',    
        },
        secondary: {
          light: '#34D399',  // Tailwind's default green-400
          DEFAULT: '#10B981', // Tailwind's default green-500
          dark: '#059669',    // Tailwind's default green-600
        },
        accent: {
          light: '#F59E0B',  // Tailwind's default yellow-500
          DEFAULT: '#EEEEEE', // Tailwind's default yellow-600
          dark: '#B45309',    // Tailwind's default yellow-700
        },
        neutral: {
          light: '#F3F4F6',  // Tailwind's default gray-100
          DEFAULT: '#9CA3AF', // Tailwind's default gray-400
          dark: '#111827',    // Tailwind's default gray-900
        },
      },
    },
  },
  plugins: [],
}

