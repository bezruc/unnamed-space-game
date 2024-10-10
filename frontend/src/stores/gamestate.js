import { ref } from "vue"
import { defineStore } from "pinia"

import sessionPhase from "@/models/sessionPhase"
import sessionPlayerStatus from "@/models/sessionPlayerStatus"

export const useGameStateStore = defineStore("game-phase", () => {
  let ships = ref([
    {
      id: 1,
      name: "Ship 1",
      allegiance: "Redtards",
      color: "red",
      position: {
        x: 100,
        y: 100
      }
    },
    {
      id: 2,
      name: "Ship 2",
      allegiance: "Greentards",
      color: "green",
      position: {
        x: 200,
        y: 200
      }
    },
    {
      id: 3,
      name: "Ship 3",
      allegiance: "Bluetards",
      color: "blue",
      position: {
        x: 300,
        y: 300
      }
    },
    {
      id: 4,
      name: "Ship 4",
      allegiance: "Azuretards",
      color: "azure",
      position: {
        x: 400,
        y: 400
      }
    }
  ])

  let selectedShip = ref({})

  const selectShip = (searchId) => {
    const result = ships.value.find(({ id }) => id == searchId)
    if (result) {
      selectedShip.value = result
      return true
    } else {
      return false
    }
  }

  const deselectShip = () => {
    selectedShip.value = {}
  }

  let currentUserId = ref(1)

  let sessions = ref([
    {
      id: 1,
      name: "party hrad",
      created: new Date(Date.now() + 100005100).toISOString(),
      phase: sessionPhase[1],
      activityLog: ["player 1 created lobby"],
      players: [
        {
          id: 1,
          name: "Derg",
          faction: "blue",
          isOwner: true,
          status: sessionPlayerStatus[0]
        },
        {
          id: 2,
          name: "Bezruc",
          faction: "red",
          isOwner: false,
          status: sessionPlayerStatus[0]
        },
        {
          id: 3,
          name: "UnknownPlayer",
          faction: "green",
          isOwner: false,
          status: sessionPlayerStatus[0]
        }
      ]
    },
    {
      id: 2,
      name: "something",
      created: new Date(Date.now()).toISOString(),
      phase: sessionPhase[0],
      activityLog: ["player 2 created lobby", "player 3 left the lobby"],
      players: [
        {
          id: 4,
          name: "Gred",
          faction: "blue",
          isOwner: false,
          status: sessionPlayerStatus[0]
        },
        {
          id: 5,
          name: "Curzeb",
          faction: "red",
          isOwner: true,
          status: sessionPlayerStatus[0]
        },
        {
          id: 6,
          name: "Noman",
          faction: "green",
          isOwner: false,
          status: sessionPlayerStatus[2]
        },
        {
          id: 1,
          name: "Derg",
          faction: "blue",
          isOwner: false,
          status: sessionPlayerStatus[0]
        }
      ]
    }
  ])

  return {
    currentUserId,
    ships,
    selectedShip,
    selectShip,
    deselectShip,
    sessions
  }
})
