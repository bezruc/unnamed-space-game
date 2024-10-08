import config from "@/config.json"

export default function () {
  const baseUrl = config.apiUrl

  const fetchApi = (method, path) => {
    const url = new URL(path, baseUrl)
    return fetch(url, {
      method: method
    })
  }

  const GET = (path) => {
    return fetchApi("GET", path)
  }

  const POST = (path) => {
    return fetchApi("POST", path)
  }

  const PUT = (path) => {
    return fetchApi("PUT", path)
  }

  const DELETE = (path) => {
    return fetchApi("DELETE", path)
  }

  return { GET, POST, PUT, DELETE }
}
