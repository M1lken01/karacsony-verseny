/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,vue}'],
  theme: {
    extend: {
      colors: {
        fg100: '#ffffff',
        fg200: '#f9f9f9',
        bg100: '#000000',
        bg200: '#111111',
        bg300: '#161616',
        bg400: '#1a1a1a',
        bg500: '#1f1f1f',
        ac100: '#3b82f6',
      },
    },
  },
  plugins: [],
};
