/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['poppins', 'sans-serif'],
      }, 
      colors: {
        primary: {
          light: '#EBF8FF',
          DEFAULT: '#4299E1',
          dark: '#2B6CB0'
        },
        secondary: {
          light: '#F7FAFC',
          DEFAULT: '#EDF2F7',
          dark: '#E2E8F0'
        },
        accent: {
          light: '#F7FAFC',
          DEFAULT: '#A0AEC0',
          dark: '#718096'
        },
        neutral: {
          light: '#F7FAFC',
          DEFAULT: '#1A202C',
          dark: '#2D3748'
        }
      },
    },
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}

