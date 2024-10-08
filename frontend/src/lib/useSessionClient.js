import { useGameStateStore } from "@/stores/gamestate"
import useApiClient from "./useApiClient"

export default function () {
  const client = useApiClient()

  const {} = useGameStateStore()

  const create = (sessionName) => {}
}
