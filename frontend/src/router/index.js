import Vue from "vue";
import VueRouter from "vue-router";
import ItemsView from "@/views/ItemsView.vue";
import BoxView from "@/views/BoxView.vue";
import CapacityQuotation from "@/views/CapacityQuotation.vue"

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
  {
    path: "/capacity-quotation",
    name: "capacity-quotation",
    component: CapacityQuotation,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
