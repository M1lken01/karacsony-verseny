<template>
  <section id="more" class="grid grid-cols-1 md:grid-cols-2 min-h-screen bg-bg300 p-0">
    <div class="order-0 md:order-none img" id="img1"></div>
    <div class="m-20 order-1 md:order-none">
      <h3 class="text-xl font-bold pb-4">x</h3>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </div>
    <div class="m-20 order-3 md:order-none">
      <h3 class="text-xl font-bold pb-4">xxx</h3>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </div>
    <div class="order-2 md:order-none img" id="img2"></div>
  </section>
</template>

<script>
export default {
  name: 'CrossSection',
};
</script>

<style scoped>
#img1 {
  background-image: url('../assets/media/szakkor1.jpg');
}

#img2 {
  background-image: url('../assets/media/szakkor2.jpg');
}

.img {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  min-height: 50vh;
  min-height: 50dvh;
}
</style>
