<script setup>
import HexRow from "./HexRow.vue"

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
  <HexRow :columns v-for="row in rows" :key="row" />
</template>

<style></style>
