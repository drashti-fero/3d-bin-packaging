<template>
  <v-dialog v-model="openDialog" width="50%" scrollable>
    <v-card>
      <v-card-title class="primary white--text">
        <v-row>
          <v-col>
            <h5>Add Box</h5>
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
        <v-form ref="boxForm">
          <v-row class="ma-0">
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                required
                class="background-white rounded-lg"
                dense
                label="Packaging Space ID*"
                :rules="[(v) => !!v || `Packaging Space ID is required`]"
                v-model="boxForm.packaging_space_id"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Length*"
                required
                :rules="[(v) => !!v || `Length is required`]"
                v-model="boxForm.length"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Width*"
                required
                :rules="[(v) => !!v || `Width is required`]"
                v-model="boxForm.width"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Height*"
                required
                :rules="[(v) => !!v || `Height is required`]"
                v-model="boxForm.height"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Weight*"
                required
                :rules="[(v) => !!v || `Weight is required`]"
                v-model="boxForm.weight"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Max Weight Capacity*"
                required
                :rules="[(v) => !!v || `Max Weight Capacity is required`]"
                v-model="boxForm.max_weight_capacity"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-select
                outlined
                hide-details="auto"
                class="background-white rounded-lg"
                dense
                label="Packaging*"
                required
                :rules="[(v) => !!v || `Max Weight Capacity is required`]"
                v-model="boxForm.packaging_type"
                :items="packagingList"
                item-text="label"
                item-value="value"
              ></v-select>
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
      boxForm: {},
      packagingList: [
        {
          label: "Box",
          value: "box",
        },
        {
          label: "Create",
          value: "create",
        },
        {
          label: "Container",
          value: "container",
        },
        {
          label: "Pallet",
          value: "pallet",
        },
        {
          label: "Vehicle",
          value: "vehicle",
        },
      ],
    };
  },

  methods: {
    resetForm() {
      this.openDialog = false;

      this.$refs.boxForm.reset();
      this.$refs.boxForm.resetValidation();
    },
    submitForm() {
      let data = { ...this.boxForm };

      this.$api.boxes
        .addBox(data)
        .then((res) => {
          this.$bus.$emit("showToastMessage", {
            message: "Box Added Successfully!",
            color: "success",
          });
          this.resetForm();
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