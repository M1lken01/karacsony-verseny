<template>
  <section id="gallery" class="flex flex-col">
    <h2 class="section-title">Galéria</h2>
    <div class="flex flex-1 flex-col justify-center p-0 md:px-12">
      <div class="flex justify-center items-center">
        <button class="scroll" @click="prevImage">&lt;</button>
        <div class="flex flex-1 p-0 md:px-12 justify-center items-center gap-8 flex-col md:gap-0 md:flex-row">
          <img class="gallery max-h-screen" :src="images[currentIndex].img" alt="Gallery Image" />
        </div>
        <button class="scroll" @click="nextImage">&gt;</button>
      </div>
      <div class="m-8 text-center">
        <p>{{ images[currentIndex].title }}</p>
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
        { img: require('../assets/media/csapatkap_fll.jpg'), title: 'FLL verseny' },
        { img: require('../assets/media/csapatkep_fll2.jpg'), title: 'FLL verseny' },
        { img: require('../assets/media/csapatkep_hajdu.jpg'), title: 'Hajdúböszörményi Robotolimpia' },
        { img: require('../assets/media/csapatkep_regi.jpg'), title: 'Régi csapat' },
        { img: require('../assets/media/csapatkep.jpg'), title: 'FLL verseny oklevél' },
        { img: require('../assets/media/fll1.jpg'), title: 'FLL verseny tesztfutamok' },
        { img: require('../assets/media/fll2.jpg'), title: 'Régi FLL verseny' },
        { img: require('../assets/media/fll3.jpg'), title: 'Innovációs projekt előadás' },
        { img: require('../assets/media/fll4.jpg'), title: 'Éles verseny' },
        { img: require('../assets/media/fll5.jpg'), title: 'Verseny nézőtér' },
        { img: require('../assets/media/fll6.jpg'), title: 'Éles verseny robotindítás' },
        { img: require('../assets/media/fll7.jpg'), title: 'Díjátadás' },
        { img: require('../assets/media/hajdu1.jpg'), title: 'Robotolimpia sumó' },
        { img: require('../assets/media/hajdu2.jpg'), title: 'Robotolimpia sumó pályák' },
        { img: require('../assets/media/hajdu3.jpg'), title: 'Robotolimpia labirintus' },
        { img: require('../assets/media/hajdu4.jpg'), title: 'Robotolimpia eredményosztás' },
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
  height: 80svh;
  object-fit: contain;
}
</style>
