<script setup>
  import { computed } from "vue"

  const { row, column } = defineProps({
    row: {
      type: Number,
      required: true
    },
    column: {
      type: Number,
      required: true
    }
  })

  const rowSpan = computed(() => {
    if (column % 2 != 0) {
      return { start: row * 2 - 1, end: row * 2 + 1 }
    } else {
      return { start: row * 2, end: row * 2 + 2 }
    }
  })
</script>

<template>
  <div class="hexagon"></div>
</template>

<style scoped>
  .hexagon {
    float: left;
    height: var(--h-hextile); /* adjust to control the size  */
    aspect-ratio: 1 / cos(30deg);
    clip-path: polygon(50% -50%, 100% 50%, 50% 150%, 0 50%);
    background: var(--c-primary-bg);
    color: white;
    grid-row: v-bind("rowSpan.start") / v-bind("rowSpan.end");
    grid-column: v-bind(column);
  }

  .hexagon:hover {
    background: var(--c-secondary-bg);
  }
</style>
