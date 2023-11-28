<template>
  <HeroSection />
  <img alt="Vue logo" src="./assets/logo.png" />
  <div class="card">somecontent</div>
  <a href="#" target="_blank" rel="noopener" class="button">read more</a>
  <input type="text" class="input" />
  <FooterSection />
</template>

<script>
import HeroSection from './components/HeroSection.vue';
import FooterSection from './components/FooterSection.vue';

export default {
  name: 'App',
  components: {
    HeroSection,
    FooterSection,
  },
};
</script>
