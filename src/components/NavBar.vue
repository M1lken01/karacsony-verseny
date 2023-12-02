<template>
  <nav class="flex justify-center sticky -top-1 bg-bg500 text-fg200 px-6 z-50">
    <div class="w-full flex justify-between items-baseline md:items-center">
      <a href="#app" class="p-6 text-xl text-fg200 font-bold hover:text-transparent hover:bg-clip-text hover:bg-gradient-to-tr from-pink-600 to-indigo-500">
        Home
      </a>
      <div class="hidden md:flex">
        <nav-item :id="'preview'" :name="'Preview'" />
        <nav-item :id="'gallery'" :name="'Gallery'" />
        <nav-item :id="'more'" :name="'FAQ'" />
        <nav-item :id="'about'" :name="'About'" />
      </div>
      <div v-if="isMenuOpen" class="md:hidden flex flex-1 flex-col items-end">
        <nav-item :id="'preview'" :name="'Preview'" />
        <nav-item :id="'gallery'" :name="'Gallery'" />
        <nav-item :id="'more'" :name="'FAQ'" />
        <nav-item :id="'about'" :name="'About'" />
      </div>
      <button class="md:hidden px-3 py-2" @click="toggleMenu">☰</button>
    </div>
  </nav>
</template>

<script>
import NavItem from '@/components/NavItem.vue';

export default {
  name: 'NavBar',
  components: {
    NavItem,
  },
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>
nav {
  background: #111111df;
  backdrop-filter: blur(4px);
  /*top: -1px*/
}
</style>
