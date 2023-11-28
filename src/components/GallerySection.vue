<template>
  <section id="gallery" class="flex p-0 md:px-12 flex-col">
    <h2 class="mx-8 mt-8 -mb-8 text-left text-2xl">Gallery</h2>
    <div class="flex flex-1 flex-col justify-center">
      <div class="flex justify-center items-center">
        <button class="scroll">&lt;</button>
        <div class="flex flex-1 p-0 md:px-12 justify-center items-center gap-8 flex-col md:gap-0 md:flex-row">
          <img class="max-h-screen" src="../assets/media/csapatkep_fll2.jpg" alt="kep" />
        </div>
        <button class="scroll">&gt;</button>
      </div>
      <div class="m-8 text-center">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'GallerySection',
};
</script>

<style scoped>
.gallery {
  max-height: 36rem;
}

.scroll {
  @apply bg-bg300 hover:bg-bg200 h-32 w-10 md:w-24;
}
</style>
