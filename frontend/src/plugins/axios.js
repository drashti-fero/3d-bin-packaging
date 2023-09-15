import router from "@/router";
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
});

// axiosInstance.interceptors.request.use((config) => {
//   return config;
// });

// axiosInstance.interceptors.response.use(
//   (config) => {
//     return config;
//   },
//   (err) => {
//     console.log(err);
//     // if (
//     //   err.response.status == 404 ||
//     //   err.response.status == 403 ||
//     //   err.response.status == 401
//     // ) {
//     //   // router.push({
//     //   //   name: "error-page",
//     //   //   params: { status: err.response.status },
//     //   // });
//     //   console.log("error", err.re)
//     // }
//     throw err;
//   }
// );

export default axiosInstance;
