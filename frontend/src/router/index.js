import { createRouter, createWebHistory } from "vue-router"
import GameView from "@/views/GameView.vue"
import LobbyView from "@/views/LobbyView.vue"
import GameMap from "@/components/GameMap.vue"
import GameList from "@/components/GameList.vue"
import GameSettings from "@/components/GameSettings.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "game",
      component: GameView,
      children: [
        {
          path: "/",
          name: "map",
          component: GameMap
        },
        {
          path: "/",
          name: "list",
          component: GameList
        },
        {
          path: "/",
          name: "settings",
          component: GameSettings
        }
      ]
    },
    {
      path: "/lobby",
      name: "lobby",
      component: LobbyView
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/View.vue')
    }
  ]
})

export default router
