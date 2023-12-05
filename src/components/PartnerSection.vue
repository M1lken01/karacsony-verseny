<template>
  <section id="partners" class="flex flex-col text-bg200 bg-fg500">
    <h2 class="section-title">Partners</h2>
    <div class="flex-1 grid grid-cols-2 md:grid-cols-3 mx-2 md:mx-16">
      <PartnerItem v-for="partner in partners" :key="partner.id" :imgSrc="partner.imgSrc" :alt="partner.alt" :link="partner.link" />
    </div>
  </section>
</template>

<script>
import PartnerItem from '@/components/PartnerItem.vue';

export default {
  name: 'PartnerSection',
  components: {
    PartnerItem,
  },
  data() {
    return {
      partners: [
        { id: 1, imgSrc: require('@/assets/brand/logo-bolyai.png'), alt: 'Bolyai Logo', link: 'https://bolyaitechnikum.hu/' },
        { id: 2, imgSrc: require('@/assets/brand/logo-blockbreakers.png'), alt: 'Blockbreakers Logo', link: 'https://www.facebook.com/BlockBreakersBolyai/' },
        { id: 3, imgSrc: require('@/assets/brand/fll-logo-horizontal.png'), alt: 'FLL Logo', link: 'https://www.firstlegoleague.hu/' },
        { id: 4, imgSrc: require('@/assets/brand/mobilis.png'), alt: 'Mobilis Logo', link: 'https://mobilis-gyor.hu/' },
        { id: 5, imgSrc: require('@/assets/brand/smr.png'), alt: 'SMR Logo', link: 'https://www.smr-automotive.com/en/global/mosonmagyarovar/' },
        { id: 6, imgSrc: require('@/assets/brand/motherson.png'), alt: 'Motherson Logo', link: 'https://www.motherson.com/' },
      ],
    };
  },
};
</script>
