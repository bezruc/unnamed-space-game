<script setup>
  import { RouterView } from "vue-router"
</script>

<template>
  <main class="layout-part">
    <router-view />
  </main>
</template>

<style scoped>
  main {
    height: calc(100vh - var(--h-main-offset));
    display: flex;
  }
</style>
