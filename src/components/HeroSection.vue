<template>
  <section class="flex">
    <div class="flex flex-1 flex-col">
      <div>
        <h1 class="py-4 text-4xl md:text-6xl font-bold">Tehetségműhely</h1>
        <p class="mb-8 text-lg text-fg500">Építjük a Jövő Robotikus Tehetségeit!</p>
        <a href="#about" class="button large-button">read more</a>
        <!--<a href="#about" target="_blank" rel="noopener" class="button">read more</a>-->
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection',
};
</script>

<style scoped>
.large-button {
  @apply p-5;
}
</style>
