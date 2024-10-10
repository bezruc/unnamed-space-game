<script setup>
  import { useGameStateStore } from "@/stores/gamestate"
  import { storeToRefs } from "pinia"
  import LobbyDialog from "./LobbyDialog.vue"
  import { ref } from "vue"
  import LobbyDetail from "./LobbyDetail.vue"

  const gameState = useGameStateStore()

  const { sessions, currentUserId } = storeToRefs(gameState)

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

  let visibleDetails = ref(false)
  let detailsSession = ref({})

  const openDetails = (session) => {
    detailsSession.value = session
    visibleDetails.value = true
  }

  const closeDetails = () => {
    visibleDetails.value = false
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
    <LobbyDetail
      :isVisible="visibleDetails"
      :session="detailsSession"
      :currentUserId
      @close-dialog="closeDetails"
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
        <li class="session-list-item" v-for="session in sessions" :key="session.id">
          <div>{{ session.name }}</div>
          <div>{{ session.id }}</div>
          <div>{{ session.created }}</div>
          <button @click="() => openDetails(session)">Details</button>
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
</style>
