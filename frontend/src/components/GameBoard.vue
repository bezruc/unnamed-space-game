<script setup>
  import { RouterView } from "vue-router"
</script>

<template>
  <div class="gameboard">
    <router-view />
  </div>
</template>

<style scoped>
  .gameboard {
    width: calc(100vw - var(--w-gamemap-offset));
    background-color: var(--c-primary-space);
  }
</style>
