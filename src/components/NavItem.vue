<template>
  <a :href="`#${id}`" :class="{ 'active-link': isActive }" @click="setActiveLink(id)" class="nav-link">
    {{ name }}
  </a>
</template>

<script>
export default {
  props: {
    id: String,
    name: String,
  },
  methods: {
    isActive(linkId) {
      return window.location.hash.replace('#', '') === linkId;
    },
    setActiveLink(linkId) {
      this.isActive = window.location.hash.replace('#', '') === linkId;
      this.$emit('update-active-link', linkId);
    },
  },
  mounted() {
    this.isActive = window.location.hash.replace('#', '') === this.id;
  },
};
</script>
