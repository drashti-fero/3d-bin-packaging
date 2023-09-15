<template>
  <div>
    <v-row class="ma-0">
      <v-col cols="6">
        <h3>Box</h3>
      </v-col>
      <v-col cols="6" class="d-flex justify-end">
        <v-btn class="primary" @click="openBoxDialog = true"> Add Box </v-btn>
      </v-col>
      <v-col cols="12">
        <AgGridVue
          @grid-ready="gridReady"
          :grid-options="gridOptions"
          :column-defs="boxHeader"
          :default-col-def="defaultColDef"
          :row-data="boxList"
          style="width: 100%; height: calc(100vh - 650px)"
          class="ag-theme-alpine"
        >
        </AgGridVue>
      </v-col>
    </v-row>

    <div id="dialogs">
      <BoxForm v-model="openBoxDialog" @refreshData="getBoxList" />
    </div>
  </div>
</template>

<script>
import { AgGridVue } from "ag-grid-vue";
import BoxForm from "../components/box/BoxForm.vue";
export default {
  name: "Box-Master",

  components: { AgGridVue, BoxForm },
  data() {
    return {
      boxList: [],
      boxHeader: [
        {
          headerName: `Packaging Space ID`,
          field: "packaging_space_id",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Packaging Type`,
          field: "packaging_type",
          sortable: true,
          minWidth: 120,
          cellStyle: {
            "text-transform": "capitalize",
          },
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
        {
          headerName: `Max Weight Capacity`,
          field: "max_weight_capacity",
          sortable: true,
          minWidth: 120,
        },
        {
          headerName: `Packaging Type`,
          field: "packaging_type",
          sortable: true,
          minWidth: 120,
        },
      ],
      openBoxDialog: false,

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
    getBoxList(params) {
      this.$bus.$emit("showLoader", true);
      this.$api.boxes
        .getBoxList(params)
        .then((result) => {
          this.boxList = result.data.data;
          this.$bus.$emit("showLoader", false);
        })
        .catch((err) => {
          console.log(err);
          this.$bus.$emit("showLoader", false);
        });
    },
  },
  mounted() {
    this.getBoxList();
  },
};
</script>
