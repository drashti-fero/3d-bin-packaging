import axiosInstance from "./axios";
import items from "@/services/items";
import boxes from "@/services/boxes";

export default {
  items: items(axiosInstance),
  boxes: boxes(axiosInstance),
};
