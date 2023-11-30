<template>
  <nav class="flex justify-center sticky top-0 bg-bg500 text-fg200 px-6">
    <div class="container flex justify-between items-center">
      <a
        href="#app"
        class="px-6 py-7 text-xl text-fg200 font-bold hover:text-transparent hover:bg-clip-text hover:bg-gradient-to-tr from-pink-600 to-indigo-500"
      >
        Home
      </a>
      <div>
        <a href="#preview" class="px-6 py-7 text-fg200 hover:text-transparent hover:bg-clip-text hover:bg-gradient-to-tr from-pink-600 to-indigo-500">
          Preview</a
        >
        <a href="#gallery" class="px-6 py-7 text-fg200 hover:text-transparent hover:bg-clip-text hover:bg-gradient-to-tr from-pink-600 to-indigo-500"
          >Gallery</a
        >
        <a href="#about" class="px-6 py-7 text-fg200 hover:text-transparent hover:bg-clip-text hover:bg-gradient-to-tr from-pink-600 to-indigo-500">About</a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style scoped>
nav {
  background: #111111df;
  backdrop-filter: blur(4px);
}
</style>
