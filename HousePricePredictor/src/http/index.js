import axios from 'axios'
 const APIUrl = 'http://127.0.0.1:8000/api/'

const getAPI = axios.create({
  baseURL: APIUrl,
  headers: {
    contentType: 'application/json',
  },
  
})   

export {getAPI }