<template>
  <section id="about" class="flex flex-col text-bg200 bg-fg500">
    <h2 class="mx-8 mt-8 -mb-8 text-left text-2xl">About</h2>
    <div class="flex flex-1 items-center my-24">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-8 px-10 md:px-32">
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
          :bulletPoints="
            JSON.parse(
              `[&quot;Jelentkezni a <a href=\\&quot;https://www.facebook.com/BlockBreakersBolyai/\\&quot; target=\\&quot;_blank\\&quot; rel=\\&quot;noopener\\&quot;>Facebook oldalunkon</a>.&quot;, &quot;Személyesen Vinnai Zsolt tanár úrnál.&quot;, &quot;Illetve Kullai Viktória tanárnőnél, az iskola tanárijában.&quot;]`,
            )
          "
        />
      </div>
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
