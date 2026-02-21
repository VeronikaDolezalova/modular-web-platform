/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './blog/templates/**/*.html',
    ],
    theme: {
      extend: {
        colors: {
          forest: '#1a4a2e',
          gold: '#c8922a',
          cream: '#f8f5f0',
        },
      },
    },
  }