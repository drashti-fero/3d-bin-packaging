import { item } from "@/utils/urlConstants";

export default ({ get, post, put }) => ({
  getItemList(params = {}) {
    return get(`${item.base}`, {
      params: params,
    });
  },
  getItemSelectList(params = {}) {
    return get(`${item.base}select/`, {
      params: params,
    });
  },
  getItemObject(id) {
    return get(`${item.base}${id}/`);
  },
  addItem(data) {
    return post(`${item.base}`, data);
  },
  updateItem(data, id) {
    return put(`${item.base}${id}/`, data);
  },
});
