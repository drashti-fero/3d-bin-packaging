<template>
  <v-app>
    <!-- <AppBar @toggleDrawer="drawer = !drawer" /> -->
    <BaseSnackbar
      v-model="showToastMessage"
      :color="snackBarColor"
      :message="snackbarMessage"
    />
    <BaseDefaultLoader :isLoader="showLoader" />
    <SideNavigation v-model="drawer" />

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import BaseDefaultLoader from "./components/BaseDefaultLoader.vue";
import BaseSnackbar from "./components/BaseSnackbar.vue";
import SideNavigation from "./components/SideNavigation.vue";
export default {
  name: "App",
  components: {
    SideNavigation,
    BaseSnackbar,
    BaseDefaultLoader,
  },

  data: () => ({
    drawer: true,
    showToastMessage: false,
    snackBarColor: "primary",
    snackbarMessage: "",
    showLoader: false,
  }),
  mounted() {
    this.$bus.$on("showToastMessage", ({ color, message }) => {
      this.snackBarColor = color;
      this.snackbarMessage = message;
      this.showToastMessage = true;
    });
    this.$bus.$on("showLoader", (value) => {
      this.showLoader = value;
    });
  },
  beforeDestroy() {
    this.$bus.$off("showToastMessage");
    this.$bus.$off("showLoader");
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/base.scss";
</style>
