import axios from 'axios'
import.meta.env.VITE_SERVER_NAME

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
})


apiClient.interceptors.request.use((request) => {
  const accessToken = JSON.parse(localStorage.getItem('token'))
  console.log(accessToken)
  if (accessToken) {
    request.headers.Authorization = `Bearer ${accessToken}`
    request.headers.AccessToken = accessToken
  }
  return request
})

apiClient.interceptors.response.use(undefined, (error) => {
  // Errors handling
  const { response } = error
  console.log()
})

export default apiClient
