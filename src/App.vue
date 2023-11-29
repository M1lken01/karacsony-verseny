<template>
  <HeroSection />
  <PreviewSection />
  <GallerySection />
  <CrossSection />
  <AboutSection />
  <FooterSection />
</template>

<script>
import HeroSection from './components/HeroSection.vue';
import PreviewSection from './components/PreviewSection.vue';
import GallerySection from './components/GallerySection.vue';
import CrossSection from './components/CrossSection.vue';
import AboutSection from './components/AboutSection.vue';
import FooterSection from './components/FooterSection.vue';

export default {
  name: 'App',
  components: {
    HeroSection,
    PreviewSection,
    GallerySection,
    CrossSection,
    AboutSection,
    FooterSection,
  },
};
</script>
