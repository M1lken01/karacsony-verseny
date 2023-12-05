<template>
  <div class="flex justify-center items-center md:m-16">
    <a :href="link">
      <img :src="imgSrc" :alt="alt" class="max-h-32 md:max-h-48 object-contain" />
    </a>
  </div>
</template>

<script>
export default {
  props: {
    imgSrc: String,
    alt: String,
    link: String,
  },
};
</script>
