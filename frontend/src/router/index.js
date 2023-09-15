import Vue from "vue";
import VueRouter from "vue-router";
import ItemsView from "@/views/ItemsView.vue";
import BoxView from "@/views/BoxView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "items",
    component: ItemsView,
  },
  {
    path: "/boxes",
    name: "boxes",
    component: BoxView,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
