<script setup>
  import { RouterView } from "vue-router"
</script>

<template>
  <div class="gameboard">
    <router-view v-slot="{ Component }">
      <keep-alive>
        <component :is="Component" />
      </keep-alive>
    </router-view>
  </div>
</template>

<style scoped>
  .gameboard {
    width: calc(100vw - var(--w-gamemap-offset));
    background-color: var(--c-primary-space);
    align-items: center;
    justify-content: center;
    display: flex;
  }
</style>
