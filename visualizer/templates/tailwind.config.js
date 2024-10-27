/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/upload.html", "../templates/visualization.html"],
  darkMode: true,
  theme: {
    extend: {
      colors: {
        text: "#e5e6e5",
        background: "#0a0b09",
        primary: "#b1c8a7",
        secondary: "#4b7439",
        accent: "#88c86a",
      },
    },
  },
  plugins: [],
};
