<template>
  <nav class="flex justify-center sticky -top-1 bg-bg500 text-fg200 md:px-6 z-50">
    <div class="w-full flex justify-between items-baseline md:items-center">
      <a href="#app" class="nav-link nav-header">Robotika</a>
      <div :class="{ 'hidden md:flex': !isMenuOpen, 'md:hidden flex flex-1 flex-col items-end': isMenuOpen }">
        <nav-item v-for="item in menuItems" :key="item.id" :id="item.id" :name="item.name" />
      </div>
      <button class="md:hidden px-3 py-2 nav-link" @click="toggleMenu">☰</button>
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
      menuItems: [
        { id: 'preview', name: 'Bemutató' },
        { id: 'gallery', name: 'Galéria' },
        { id: 'partners', name: 'Partnerek' },
        { id: 'more', name: 'Infó' },
        { id: 'about', name: 'Jelentkezés' },
      ],
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
}
</style>
