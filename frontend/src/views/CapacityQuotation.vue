<template>
  <div>
    <v-row class="ma-0">
      <v-col>
        <h3>Capacity Quotation</h3>
      </v-col>
    </v-row>

    <v-card elevation="0">
      <v-card-text>
        <v-form ref="capacityQuotationForm" class="pa-5">
          <v-row>
            <v-col>
              <v-text-field
                outlined
                hide-details="auto"
                required
                class="background-white rounded-lg"
                dense
                label="Ref No*"
                :rules="[(v) => !!v || `Ref No is required`]"
                v-model="capacityQuotation.ref_no"
              ></v-text-field>
            </v-col>
            <v-col>
              <v-select
                outlined
                hide-details="auto"
                required
                class="background-white rounded-lg"
                dense
                multiple
                label="Bins*"
                :rules="[(v) => !!v || `Bins is required`]"
                v-model="capacityQuotation.bins"
                :items="binsList"
                item-text="packaging_space_id"
                item-value="id"
              ></v-select>
            </v-col>

            <v-col cols="12">
              <v-row>
                <v-col cols="12">
                  <h3>Add Items</h3>
                </v-col>

                <v-col cols="12" v-for="(item, index) in items" :key="index">
                  <v-row>
                    <v-col>
                      <v-select
                        outlined
                        hide-details="auto"
                        required
                        class="background-white rounded-lg"
                        dense
                        label="Items*"
                        v-model="item.id"
                        :items="itemsList"
                        item-text="sku"
                        item-value="id"
                      ></v-select>
                    </v-col>
                    <v-col>
                      <v-text-field
                        outlined
                        hide-details="auto"
                        required
                        class="background-white rounded-lg"
                        dense
                        label="Quantity*"
                        :rules="[(v) => !!v || `Quantity is required`]"
                        v-model="item.quantity"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-btn
                        id="addItem"
                        :small="$vuetify.breakpoint.xl"
                        :x-small="$vuetify.breakpoint.lgAndDown"
                        class="primary elevation-0 py-5 rounded-lg mr-4"
                        @click="addItem()"
                      >
                        <v-icon>mdi-plus</v-icon>
                      </v-btn>
                      <v-btn
                        id="removeItem"
                        :small="$vuetify.breakpoint.xl"
                        :x-small="$vuetify.breakpoint.lgAndDown"
                        v-if="items.length > 1"
                        class="light_grey elevation-0 py-5 rounded-lg"
                        @click="removeItem(index)"
                      >
                        <v-icon>mdi-minus</v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>

      <v-card-actions class="d-flex justify-end">
        <v-btn class="primary" @click="submitForm">Submit</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      capacityQuotation: {},
      binsList: [],
      itemsList: [],
      items: [{}],
    };
  },
  methods: {
    getBoxList(params) {
      this.$bus.$emit("showLoader", true);
      this.$api.boxes
        .getBoxList(params)
        .then((result) => {
          this.binsList = result.data.data;
          this.$bus.$emit("showLoader", false);
        })
        .catch((err) => {
          console.log(err);
          this.$bus.$emit("showLoader", false);
        });
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
    removeItem(index) {
      this.items.splice(index, 1);
    },
    addItem() {
      this.items.push({});
    },
    submitForm() {
      let data = { ...this.capacityQuotation, items: this.items };
      this.$api.capacityQuotation
        .addCapacityQuotation(data)
        .then((res) => {
          this.$bus.$emit("showToastMessage", {
            message: "Capacity Quotation Added Successfully!",
            color: "success",
          });
          this.closeDialog();
          this.$bus.$emit("refreshData");
        })
        .catch((err) => {
          console.log("err", err);
          this.$bus.$emit("showToastMessage", {
            message: "Something went wrong!",
            color: "error",
          });
        });
    },
  },
  mounted() {
    this.getBoxList();
    this.getItemsList();
  },
};
</script>

<style>
</style>