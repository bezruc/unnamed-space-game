<script setup>
  import { useGameStateStore } from "@/stores/gamestate"
  import { storeToRefs } from "pinia"

  const gameState = useGameStateStore()

  const { ships } = storeToRefs(gameState)

  const { selectShip, deselectShip } = gameState
</script>

<template>
  <div>
    <button @click="deselectShip">Deselect ship</button>
    <ul>
      <li v-for="(ship, index) in ships" :key="index" @click="() => selectShip(ship.id)">
        {{ ship.name }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
  li::marker {
    content: "";
  }
</style>
