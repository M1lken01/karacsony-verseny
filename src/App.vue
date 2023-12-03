<template>
  <NavBar />
  <HeroSection />
  <PreviewSection />
  <GallerySection />
  <PartnerSection />
  <CrossSection />
  <AboutSection />
  <FooterSection />
</template>

<script>
import NavBar from './components/NavBar.vue';
import HeroSection from './components/HeroSection.vue';
import PreviewSection from './components/PreviewSection.vue';
import GallerySection from './components/GallerySection.vue';
import PartnerSection from './components/PartnerSection.vue';
import CrossSection from './components/CrossSection.vue';
import AboutSection from './components/AboutSection.vue';
import FooterSection from './components/FooterSection.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    HeroSection,
    PreviewSection,
    GallerySection,
    PartnerSection,
    CrossSection,
    AboutSection,
    FooterSection,
  },
};
</script>
