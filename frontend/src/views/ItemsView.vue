<template>
  <div>
    <v-row class="ma-0">
      <v-col cols="6">
        <h3>Items</h3>
      </v-col>
      <v-col cols="6" class="d-flex justify-end">
        <v-btn class="primary" @click="openItemsDialog = true">
          Add Item
        </v-btn>
      </v-col>
      <v-col cols="12">
        <AgGridVue
          @grid-ready="gridReady"
          :grid-options="gridOptions"
          :column-defs="itemsHeader"
          :default-col-def="defaultColDef"
          :row-data="itemsList"
          style="width: 100%; height: calc(100vh - 650px)"
          class="ag-theme-alpine"
        >
        </AgGridVue>
      </v-col>
    </v-row>

    <div id="dialogs">
      <ItemsForm v-model="openItemsDialog" />
    </div>
  </div>
</template>

<script>
import { AgGridVue } from "ag-grid-vue";
import ItemsForm from "../components/items/ItemsForm.vue";
export default {
  name: "Items-Master",

  components: { AgGridVue, ItemsForm },
  data() {
    return {
      itemsList: [],
      itemsHeader: [
        {
          headerName: `Ref No`,
          field: "ref_no",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Name`,
          field: "name",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Length`,
          field: "length",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Width`,
          field: "width",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Height`,
          field: "height",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Weight`,
          field: "weight",
          sortable: true,
          minWidth: 120,
        },
      ],
      openItemsDialog: false,

      gridApi: null,
      columnApi: null,
      defaultColDef: {
        resizable: true,
        flex: 1,
        initialWidth: 200,
        wrapHeaderText: true,
        autoHeaderHeight: true,
      },
      gridOptions: {
        onGridSizeChanged: () => {
          this.gridOptions.api.sizeColumnsToFit();
        },
        headerHeight: 40,
        rowHeight: 40,
        rowSelection: "multiple",
        suppressRowClickSelection: true,
        suppressDragLeaveHidesColumns: true,
        enableCellTextSelection: true,
      },
    };
  },
  methods: {
    gridReady(params) {
      this.gridApi = params.api;
      this.columnApi = params.columnApi;
    },
    getItemsList(params) {
      this.$bus.$emit("showLoader", true);
      this.$api.items
        .getItemList(params)
        .then((result) => {
          this.itemsList = result.data.data;
          this.$bus.$emit("showLoader", false);
        })
        .catch((err) => {
          console.log(err);
          this.$bus.$emit("showLoader", false);
        });
    },
  },
  mounted() {
    this.getItemsList();
  },
};
</script>
