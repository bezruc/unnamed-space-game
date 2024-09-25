<script setup>
import HexTile from "./HexTile.vue"

defineProps({
  columns: {
    type: Number,
    required: true,
    default: 3
  }
})
</script>

<template>
  <div class="hex-row">
    <HexTile v-for="column in columns" :key="column" :is-even="column % 2 == 0"></HexTile>
  </div>
</template>

<style scoped>
.hex-row {
  clear: left;
  /* -webkit-transform: scale(0.5, 0.5);
  -moz-transform: scale(0.5, 0.5);
  transform: scale(0.5, 0.5); */
}
</style>
