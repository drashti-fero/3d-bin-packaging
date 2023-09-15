import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
});

// Request interceptor (can be removed if not needed)
axiosInstance.interceptors.request.use((config) => {
  return config;
});

// Response interceptor (can be removed if not needed)
axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.log("Error:", error);
    throw error;
  }
);

export default axiosInstance;