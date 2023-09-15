import axiosInstance from "./axios";
import items from "@/services/items";
import boxes from "@/services/boxes";
import capacityQuotation from "@/services/capacityQuotation";

export default {
  items: items(axiosInstance),
  boxes: boxes(axiosInstance),
  capacityQuotation: capacityQuotation(axiosInstance),
};
