<template>
  <nav class="flex justify-center sticky top-0 bg-bg500 text-fg200 px-6 z-50">
    <div class="container flex justify-between items-center">
      <a
        href="#app"
        class="px-6 py-7 text-xl text-fg200 font-bold hover:text-transparent hover:bg-clip-text hover:bg-gradient-to-tr from-pink-600 to-indigo-500"
      >
        Home
      </a>
      <div>
        <nav-item :id="'preview'" :name="'Preview'" @update-active-link="setActiveLink" />
        <nav-item :id="'gallery'" :name="'Gallery'" @update-active-link="setActiveLink" />
        <nav-item :id="'more'" :name="'FAQ'" @update-active-link="setActiveLink" />
        <nav-item :id="'about'" :name="'About'" @update-active-link="setActiveLink" />
      </div>
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
      activeLink: '',
    };
  },
  methods: {
    setActiveLink(linkId) {
      this.activeLink = linkId;
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
