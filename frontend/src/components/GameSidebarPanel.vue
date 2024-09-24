<script setup lang="ts">
import IconCogwheel from "./icons/IconCogwheel.vue"
import IconList from "./icons/IconList.vue"
import IconMap from "./icons/IconMap.vue"
import GameSidebarButton from "./GameSidebarButton.vue"
</script>

<template>
  <aside>
    <GameSidebarButton subroute="map" tooltip="Map">
      <template #icon>
        <IconMap />
      </template>
    </GameSidebarButton>
    <GameSidebarButton subroute="list" tooltip="List">
      <template #icon>
        <IconList />
      </template>
    </GameSidebarButton>
    <GameSidebarButton subroute="settings" tooltip="Settings">
      <template #icon>
        <IconCogwheel />
      </template>
    </GameSidebarButton>
  </aside>
</template>

<style scoped>
aside {
  height: 100%;
  min-width: var(--w-sidebar);
  border-width: 0px 2px 0px 0px;
  border-color: var(--c-primary-tx);
  border-style: solid;
  background-color: var(--c-primary-bg);
  color: var(--c-primary-tx);
}
</style>
