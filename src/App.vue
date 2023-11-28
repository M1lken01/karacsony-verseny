<template>
  <HeroSection />
  <GallerySection />
  <AboutSection />
  <img alt="Vue logo" src="./assets/logo.png" />
  <FooterSection />
</template>

<script>
import HeroSection from './components/HeroSection.vue';
import GallerySection from './components/GallerySection.vue';
import AboutSection from './components/AboutSection.vue';
import FooterSection from './components/FooterSection.vue';

export default {
  name: 'App',
  components: {
    HeroSection,
    GallerySection,
    AboutSection,
    FooterSection,
  },
};
</script>
