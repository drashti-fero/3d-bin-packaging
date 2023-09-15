import { capacityQuotation } from "@/utils/urlConstants";

export default ({ get, post, put }) => ({
  getCapacityQuotationList(params = {}) {
    return get(`${capacityQuotation.base}`, {
      params: params,
    });
  },
  getCapacityQuotationSelectList(params = {}) {
    return get(`${capacityQuotation.base}select/`, {
      params: params,
    });
  },
  getCapacityQuotationObject(id) {
    return get(`${capacityQuotation.base}${id}/`);
  },
  addCapacityQuotation(data) {
    return post(`${capacityQuotation.base}`, data);
  },
  updateCapacityQuotation(data, id) {
    return put(`${capacityQuotation.base}${id}/`, data);
  },
});
