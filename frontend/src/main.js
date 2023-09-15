import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";

import api from "@/plugins/api.js";
import axiosInstance from "@/plugins/axios.js";

Vue.prototype.$bus = new Vue();
Vue.prototype.$axios = axiosInstance;
Vue.prototype.$api = api;


Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
