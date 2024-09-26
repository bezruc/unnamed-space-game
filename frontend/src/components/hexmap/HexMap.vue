<script setup>
  import HexTile from "./HexTile.vue"

  defineProps({
    rows: {
      type: Number,
      required: true,
      default: 0
    },
    columns: {
      type: Number,
      required: true,
      default: 0
    }
  })
</script>

<template>
  <div class="grid">
    <template v-for="row in rows" :key="row">
      <HexTile v-for="column in columns" :key="column" :column :row />
    </template>
  </div>
</template>

<style scoped>
  .grid {
    display: grid;
    row-gap: var(--h-gap-grid);
    column-gap: var(--w-gap-grid);
    grid-auto-rows: calc(var(--h-grid-item) / 2);
    grid-auto-columns: var(--w-grid-item);
    justify-items: center;
  }
</style>
