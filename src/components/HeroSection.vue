<template>
  <section class="flex py-4 px-8 md:p-32 gap-24 md:gap-8 flex-col md:flex-row">
    <div class="flex flex-0 md:flex-1 flex-col">
      <div>
        <h1 class="py-6 text-4xl md:text-6xl font-bold">Tehetségműhely</h1>
        <p class="mb-12 text-lg text-fg500">Építjük a Jövő Robotikus Tehetségeit!</p>
        <a
          href="#about"
          class="p-5 text-white bg-blue-500 rounded-sm shadow-md hover:bg-blue-600 hover:text-white focus:outline-none focus:ring focus:border-blue-700"
          >read more
        </a>
        <!--<a href="#about" target="_blank" rel="noopener" class="button">read more</a>-->
      </div>
    </div>
    <div class="flex md:block justify-center">
      <img src="../assets/brand/logo.png" alt="logo" class="max-w-xs md:max-w-lg" />
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection',
};
</script>
