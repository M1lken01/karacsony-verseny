<template>
  <section id="gallery" class="flex flex-col">
    <h2 class="mx-8 mt-8 -mb-8 text-left text-2xl">Gallery</h2>
    <div class="flex flex-1 flex-col justify-center p-0 md:px-12">
      <div class="flex justify-center items-center">
        <button class="scroll" @click="prevImage">&lt;</button>
        <div class="flex flex-1 p-0 md:px-12 justify-center items-center gap-8 flex-col md:gap-0 md:flex-row">
          <img class="gallery max-h-screen" :src="images[currentIndex]" alt="Gallery Image" />
        </div>
        <button class="scroll" @click="nextImage">&gt;</button>
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
  data() {
    return {
      currentIndex: 0,
      images: [
        require('../assets/media/csapatkap_fll.jpg'),
        require('../assets/media/csapatkep_fll2.jpg'),
        require('../assets/media/csapatkep_hajdu.jpg'),
        require('../assets/media/csapatkep_regi.jpg'),
        require('../assets/media/csapatkep.jpg'),
      ],
    };
  },
  methods: {
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
  },
};
</script>

<style scoped>
.gallery {
  height: 80vh;
  height: 80dvh;
  object-fit: contain;
}
</style>
