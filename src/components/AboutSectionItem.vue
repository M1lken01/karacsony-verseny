<template>
  <div class="md:flex-1 min-w-full md:min-w-0">
    <h3 class="py-2 text-xl font-bold">{{ title }}</h3>
    <ul>
      <li v-for="point in bulletPoints" :key="point">{{ point }}</li>
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
