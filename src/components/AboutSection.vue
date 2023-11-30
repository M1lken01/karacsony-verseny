<template>
  <section id="about" class="flex flex-col text-bg200 bg-fg500">
    <h2 class="mx-8 mt-8 -mb-8 text-left text-2xl">About</h2>
    <div class="flex flex-1 px-10 md:px-32 justify-center md:justify-around items-center gap-8 flex-col md:gap-32 md:flex-row">
      <AboutSectionItem
        title="Mikor és hol vannak a szakkörök?"
        :bulletPoints="['A szakköri foglalkozások a 39-es teremben vannak, szerdánként 14:30-16:00-ig.']"
      />
      <AboutSectionItem
        title="Hogyan lehet bekerülni a tehetségműhelybe?"
        :bulletPoints="[
          'Bárki jelentkezhet, akit érdekel.',
          'Megnézzük mennyire van érzéke ezekhez a dolgokhoz.',
          'Azt fontos tudni, hogy a nevének megfelelően elsődlegesen tehetséggondozással foglalkozunk.',
        ]"
      />
      <AboutSectionItem
        title="Hogyan lehet jelentkezni?"
        :bulletPoints="[
          'Jelentkezni a Facebook oldalunkon.',
          'Személyesen Vinnai Zsolt tanár úrnál.',
          'Illetve Kullai Viktória tanárnőnél, az iskola tanárijában.',
        ]"
      />
    </div>
  </section>
</template>

<script>
import AboutSectionItem from '@/components/AboutSectionItem.vue';

export default {
  name: 'AboutSection',
  components: {
    AboutSectionItem,
  },
};
</script>
