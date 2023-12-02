<template>
  <a :href="`#${id}`" class="nav-link">
    {{ name }}
  </a>
</template>

<script>
export default {
  props: {
    id: String,
    name: String,
  },
};
</script>
