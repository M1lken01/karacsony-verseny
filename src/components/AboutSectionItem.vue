<template>
  <div class="about-item">
    <h3 class="py-2 text-xl font-bold">{{ title }}</h3>
    <ul>
      <li v-for="point in bulletPoints" :key="point" v-html="point"></li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    bulletPoints: Array,
  },
};
</script>
