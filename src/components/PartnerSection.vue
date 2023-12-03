<template>
  <section id="partner" class="flex flex-col text-bg200 bg-fg500">
    <h2 class="section-title">Partners</h2>
    <p>A tehetségműhely munkáját az utóbbi években támogatta a Mobilis és az SMR is.</p>
    <div class="flex-1 grid grid-cols-2 md:grid-cols-3 mx-2 md:mx-16">
      <PartnerItem :imgSrc="require('@//assets/brand/fll-logo-horizontal.png')" alt="FLL Logo" link="https://example.com" />
      <PartnerItem :imgSrc="require('@//assets/brand/fll-logo-horizontal.png')" alt="FLL Logo" link="https://example.com" />
      <PartnerItem :imgSrc="require('@//assets/brand/fll-logo-horizontal.png')" alt="FLL Logo" link="https://example.com" />
      <PartnerItem :imgSrc="require('@//assets/brand/fll-logo-horizontal.png')" alt="FLL Logo" link="https://example.com" />
      <PartnerItem :imgSrc="require('@//assets/brand/fll-logo-horizontal.png')" alt="FLL Logo" link="https://example.com" />
      <PartnerItem :imgSrc="require('@//assets/brand/fll-logo-horizontal.png')" alt="FLL Logo" link="https://example.com" />
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
};
</script>
