<script setup>
  import { useGameStateStore } from "@/stores/gamestate"
  import { storeToRefs } from "pinia"
  import LobbyDialog from "./LobbyDialog.vue"
  import { ref } from "vue"

  const gameState = useGameStateStore()

  const { sessions } = storeToRefs(gameState)

  let visibleCreateDialog = ref(false)
  let visibleJoinDialog = ref(false)

  const closeCreateDialog = () => {
    console.log("closing based on emitted event ")
    visibleCreateDialog.value = false
  }
  const submitCreateDialog = (lobbyName) => {
    console.log(lobbyName)
    visibleCreateDialog.value = false
  }

  const closeJoinDialog = () => {
    console.log("closing based on emitted event ")
    visibleJoinDialog.value = false
  }
  const submitJoinDialog = (lobbyId) => {
    console.log(lobbyId)
    visibleJoinDialog.value = false
  }
</script>

<template>
  <div class="lobby">
    <LobbyDialog
      :isVisible="visibleCreateDialog"
      operation-name="create"
      @close-dialog="closeCreateDialog"
      @submit-dialog="submitCreateDialog"
    />
    <LobbyDialog
      :isVisible="visibleJoinDialog"
      operation-name="join"
      @close-dialog="closeJoinDialog"
      @submit-dialog="submitJoinDialog"
    />
    <div>Session list</div>
    <div>
      <button @click="visibleCreateDialog = true">CREATE</button>
      <button @click="visibleJoinDialog = true">JOIN</button>
    </div>
    <div>
      <ul>
        <li class="session-list-item">
          <div>Name</div>
          <div>ID</div>
          <div>Created</div>
          <div>Details button</div>
        </li>
        <li class="session-list-item" v-for="lobby in sessions" :key="lobby.id">
          <div>{{ lobby.name }}</div>
          <div>{{ lobby.id }}</div>
          <div>{{ lobby.created }}</div>
          <button>Details</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
  .lobby {
    width: calc(100vw);
    background-color: var(--c-primary-space);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    align-content: left;
    display: flex;
    position: relative;
  }

  .session-list-item {
    height: 3rem;
    display: flex;
    justify-content: space-between;
    border-bottom: 2px solid var(--c-primary-tx);
  }

  .session-list-item > * {
    margin: auto 100px;
  }

  li {
    list-style-type: none;
  }

  /* .lobby-create-dialog {
    --width: 400px;
    --height: 200px;
    width: var(--width);
    height: var(--height);
    background-color: var(--c-secondary-bg);
    position: absolute;
    left: calc(50% - var(--width) / 2);
    top: calc(50% - var(--height) / 2);
  }
  .is-visible {
    display: none;
  } */
</style>
