<template>
  <section class="flex py-4 px-8 md:p-32 gap-24 md:gap-8 flex-col md:flex-row">
    <div class="flex flex-0 md:flex-1 flex-col flex-wrap">
      <div>
        <h1 class="py-6 text-4xl md:text-6xl font-bold">Tehetségműhely</h1>
        <p class="mb-12 text-lg text-fg500">Építjük a Jövő Robotikus Tehetségeit!</p>
        <a
          href="#preview"
          class="p-5 text-white bg-blue-500 rounded-sm shadow-md hover:bg-blue-600 hover:text-white focus:outline-none focus:ring bg-gradient-to-r from-sky-500 to-indigo-500"
          >read more
        </a>
        <!--<a href="#about" target="_blank" rel="noopener" class="button">read more</a>-->
      </div>
    </div>
    <div class="flex md:block justify-center">
      <img src="../assets/brand/fll-logo-horizontal.png" alt="Logo Image" class="w-96 max-w-xs md:max-w-3xl" />
      <!-- todo: fix size and wrap-->
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection',
};
</script>
