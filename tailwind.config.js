/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,vue}'],
  theme: {
    extend: {
      colors: {
        fg100: '#ffffff',
        fg200: '#f9f9f9',
        fg300: '#f1f1f1',
        fg400: '#e3e3e3',
        fg500: '#d5d5d5',
        bg100: '#000000',
        bg200: '#111111',
        bg300: '#161616',
        bg400: '#1a1a1a',
        bg500: '#1f1f1f',
        ac100: '#3b82f6',
        ac200: '#eb4263',
        ac300: '#eb5641',
        ac400: '#eb7342',
        ac500: '#eb9142',
        'accent-100': '#2F3CEB',
        'accent-200': '#5D2DEB',
        'accent-300': '#9B2CEA',
        'accent-400': '#DA2DEB',
        'accent-500': '#EB2D98',
      },
    },
  },
  plugins: [],
};
