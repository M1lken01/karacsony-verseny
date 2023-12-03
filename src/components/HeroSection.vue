<template>
  <section class="flex -mt-20 py-4 px-8 md:p-32 gap-24 md:gap-8 flex-col md:flex-row justify-center min-h-screen">
    <div class="flex flex-0 md:flex-1 flex-col flex-wrap">
      <div class="text-center md:text-left">
        <h1 class="py-6 text-4xl md:text-6xl font-bold">Tehetségműhely</h1>
        <p class="mb-12 text-lg text-fg500">Építjük a Jövő Robotikus Tehetségeit!</p>
        <a
          href="#preview"
          class="p-5 text-fg200 rounded-sm shadow-md hover:text-fg500 focus:outline-none bg-gradient-to-tr from-sky-500 to-indigo-500 hover:from-indigo-500 hover:to-fuchsia-500 transition-all duration-300 ease-in-out"
          >Tovább az Részletekhez
        </a>
        <!--<a href="#about" target="_blank" rel="noopener" class="button">read more</a>-->
      </div>
    </div>
    <div class="flex md:block justify-center">
      <img src="@/assets/brand/fll-logo-horizontal.png" alt="Logo Image" class="w-96 max-w-xs md:max-w-3xl" />
      <!-- todo: fix size and wrap-->
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection',
};
</script>
