<template>
  <div class="md:flex-1 min-w-full md:min-w-0 bg-fg300 p-4 md:p-8 rounded-md shadow-md hover:shadow-2xl transition-all">
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
