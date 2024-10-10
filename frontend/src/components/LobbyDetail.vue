<script setup>
  import { computed } from "vue"

  const { isVisible, session, currentUserId } = defineProps({
    isVisible: {
      type: Boolean,
      required: true,
      default: false
    },
    session: {
      required: true,
      type: {
        id: Number,
        name: String,
        created: Date,
        phase: String,
        activityLog: Array,
        players: [
          {
            id: Number,
            name: String,
            faction: String,
            isOwner: Boolean,
            status: String
          }
        ]
      }
    },
    currentUserId: {
      type: Number,
      required: true
    }
  })

  const isButtonVisible = computed(() => {
    if (isVisible) {
      let obj = {
        open: session.phase == "LIVE",
        leave: !session.players.find((e) => e.id == currentUserId)?.isOwner,
        start:
          (session.players.find((e) => e.id == currentUserId)?.isOwner ?? false) &&
          session.phase == "NEW",
        cancel:
          (session.players.find((e) => e.id == currentUserId)?.isOwner ?? false) &&
          session.phase != "COMPLETED",
        chown: session.players.find((e) => e.id == currentUserId)?.isOwner ?? false
      }
      console.log(obj)
      return obj
    } else {
      return {
        open: false,
        leave: false,
        start: false,
        cancel: false,
        chown: false
      }
    }
  })

  const emit = defineEmits(["close-dialog", "submit-dialog"])

  const close = () => {
    emit("close-dialog")
  }
</script>

<template>
  <div class="lobby-detail" :class="{ 'is-visible': isVisible }">
    <div class="flex">
      <button @click="close" id="close">CLOSE</button>
      <div>{{ session.name }} SESSION</div>
      <div>{{ session.phase }}</div>
      <ul>
        <li class="session-player">
          <div>Name</div>
          <div>Faction</div>
          <div>Owner</div>
          <div>Status</div>
        </li>
        <li
          class="session-player"
          :class="{ highlight: currentUserId == player.id }"
          v-for="player in session.players"
          :key="player.id"
        >
          <div>{{ player.name }}</div>
          <div>{{ player.faction }}</div>
          <div>{{ player.isOwner }}</div>
          <div>{{ player.Status }}</div>
        </li>
      </ul>
      <div class="controls">
        <button :class="{ 'is-visible': isButtonVisible.open }">OPEN</button>
        <button :class="{ 'is-visible': isButtonVisible.leave }">LEAVE</button>
        <button :class="{ 'is-visible': isButtonVisible.start }">START</button>
        <button :class="{ 'is-visible': isButtonVisible.cancel }">CANCEL</button>
        <button :class="{ 'is-visible': isButtonVisible.chown }">CHANGE OWNER</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .lobby-detail {
    --width: 800px;
    --height: 600px;
    width: var(--width);
    height: var(--height);
    background-color: var(--c-secondary-bg);
    position: absolute;
    left: calc(50% - var(--width) / 2);
    top: calc(50% - var(--height) / 2);
    padding: 1rem;
    display: none;
  }

  .flex {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: column;
  }

  .is-visible {
    display: block;
  }

  #close {
    align-self: flex-start;
    display: block;
  }

  .session-player {
    height: 3rem;
    display: flex;
    justify-content: space-between;
    border-bottom: 2px solid var(--c-primary-tx);
  }

  .session-player > * {
    margin: auto 50px;
  }

  li {
    list-style-type: none;
  }

  li.highlight > div {
    font-weight: 800;
  }

  .controls button {
    display: none;
  }

  .controls button.is-visible {
    display: inline-block;
  }
</style>
