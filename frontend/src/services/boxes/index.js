import { boxes } from "@/utils/urlConstants";

export default ({ get, post, put }) => ({
  getBoxList(params = {}) {
    return get(`${boxes.base}`, {
      params: params,
    });
  },
  getBoxesSelectList(params = {}) {
    return get(`${boxes.base}select/`, {
      params: params,
    });
  },
  getBoxObject(id) {
    return get(`${boxes.base}${id}/`);
  },
  addBox(data) {
    return post(`${boxes.base}`, data);
  },
  updateBox(data, id) {
    return put(`${boxes.base}${id}/`, data);
  },
});
