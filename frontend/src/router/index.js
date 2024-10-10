import { createRouter, createWebHistory } from "vue-router"
import GameView from "@/views/GameView.vue"
import LobbyView from "@/views/LobbyView.vue"
import GameMap from "@/components/GameMap.vue"
import GameOverview from "@/components/GameOverview.vue"
import GameList from "@/components/GameList.vue"
import GameSettings from "@/components/GameSettings.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/lobby"
    },
    {
      path: "/game",
      name: "game",
      component: GameView,
      children: [
        {
          path: "/game",
          name: "overview",
          component: GameOverview
        },
        {
          path: "/game/map",
          name: "map",
          component: GameMap
        },
        {
          path: "/game/list",
          name: "list",
          component: GameList
        },
        {
          path: "/game/settings",
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
