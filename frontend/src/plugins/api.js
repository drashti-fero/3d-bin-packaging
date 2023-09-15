import axiosInstance from "./axios";
import items from "@/services/items";


export default {
  items: items(axiosInstance),
};
