<script setup>
import { RouterLink } from "vue-router"

const routes = {
  game: "/",
  lobby: "/lobby"
}
</script>

<template>
  <nav class="layout-part">
    <RouterLink
      :to="routes.game"
      class="router-link"
      :class="{ 'router-link-current': $router.currentRoute.value.path == routes.game }"
      >Game</RouterLink
    >
    <RouterLink
      :to="routes.lobby"
      class="router-link"
      :class="{ 'router-link-current': $router.currentRoute.value.path == routes.lobby }"
      >Lobby</RouterLink
    >
  </nav>
</template>

<style scoped>
nav {
  height: var(--h-navbar);
}

.router-link {
  height: 100%;
  padding: 5px 10px;
  display: inline-block;
}

nav a,
nav a:visited,
nav a:active {
  color: var(--c-secondary-tx);
  text-decoration: none;
}

nav a:hover {
  color: var(--c-primary-tx);
  background-color: var(--c-secondary-bg);
}

.router-link-current {
  color: var(--c-primary-tx);
  background-color: var(--c-secondary-bg);
  font-weight: 600;
}
</style>
