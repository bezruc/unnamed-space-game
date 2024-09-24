import { ref } from "vue"
import { defineStore } from "pinia"

export const useGameStateStore = defineStore("game-state", () => {
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

  // const count = ref(0)
  // const doubleCount = computed(() => count.value * 2)
  // function appendShip() {
  //   ships.value.push({
  //     id: 3,
  //     name: "Ship 3",
  //     allegiance: "Bluetards",
  //     color: "blue",
  //     position: {
  //       x: 300,
  //       y: 300
  //     }
  //   })
  //   console.log(ships.value.length)
  // }

  return { ships, selectedShip, selectShip, deselectShip }
})
