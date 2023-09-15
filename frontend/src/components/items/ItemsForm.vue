<template>
  <v-dialog v-model="openDialog" width="50%" scrollable>
    <v-card>
      <v-card-title class="primary white--text">
        <v-row>
          <v-col>
            <h5>Add Item</h5>
          </v-col>
          <v-spacer></v-spacer>
          <v-col class="d-flex justify-end">
            <v-icon @click="openDialog = false" color="white">
              mdi-close
            </v-icon>
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text class="pa-5">
        <v-form ref="itemsForm">
          <v-row class="ma-0">
            <!-- <v-col cols="6">
              <v-text-field
                outlined
                required
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Ref No*"
                :rules="[(v) => !!v || `Ref No is required`]"
                v-model="itemsForm.ref_no"
              ></v-text-field>
            </v-col> -->
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                required
                class="background-white rounded-lg"
                dense
                label="SKU*"
                :rules="[(v) => !!v || `Name is required`]"
                v-model="itemsForm.sku"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Length(CM)*"
                required
                :rules="[(v) => !!v || `Length is required`]"
                v-model="itemsForm.length"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Width(CM)*"
                required
                :rules="[(v) => !!v || `Width is required`]"
                v-model="itemsForm.width"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Height(CM)*"
                required
                :rules="[(v) => !!v || `Height is required`]"
                v-model="itemsForm.height"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Weight(KG)*"
                required
                :rules="[(v) => !!v || `Weight is required`]"
                v-model="itemsForm.weight"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
      <v-card-actions class="d-flex justify-end">
        <v-btn outlined class="primary--text" @click="resetForm"> Reset </v-btn>
        <v-btn class="primary" @click="submitForm"> Submit </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    value: Boolean,
  },
  computed: {
    openDialog: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      },
    },
  },
  data() {
    return {
      itemsForm: {},
    };
  },

  methods: {
    resetForm() {
      this.$refs.itemsForm.reset();
      this.$refs.itemsForm.resetValidation();
    },
    closeDialog() {
      this.openDialog = false;
      this.resetForm();
    },
    submitForm() {
      let data = { ...this.itemsForm };

      this.$api.items
        .addItem(data)
        .then((res) => {
          this.$bus.$emit("showToastMessage", {
            message: "Item Added Successfully!",
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
};
</script>

<style>
</style>