<script setup>
  import { useGameStateStore } from "@/stores/gamestate"
  import { storeToRefs } from "pinia"
  import { computed } from "vue"

  const gameState = useGameStateStore()

  const { selectedShip } = storeToRefs(gameState)

  const color = computed(() => selectedShip.value.color ?? "black")
</script>

<template>
  <aside v-if="selectedShip.name">
    <p>id: {{ selectedShip.id }}</p>
    <p>name: {{ selectedShip.name }}</p>
    <p>allegiance: {{ selectedShip.allegiance }}</p>
    <p>color: {{ selectedShip.color }}</p>
    <p>x: {{ selectedShip.position.x }}</p>
    <p>y: {{ selectedShip.position.y }}</p>
  </aside>
</template>

<style scoped>
  aside {
    --c-primary-detail: v-bind(color);
    height: 100%;
    min-width: var(--w-detail);
    border-width: 0px 0px 0px 2px;
    border-color: var(--c-primary-tx);
    border-style: solid;
    background-color: var(--c-primary-bg);
    background-color: hsl(from var(--c-primary-detail) h s 10%);
    color: hsl(from var(--c-primary-detail) h s 90%);
  }
</style>
