<template>
  <v-app>
    <!-- <AppBar @toggleDrawer="drawer = !drawer" /> -->

    <SideNavigation v-model="drawer" />

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import SideNavigation from "./components/SideNavigation.vue";
export default {
  name: "App",
  components: {
    SideNavigation,
  },

  data: () => ({
    drawer: true,
  }),
};
</script>
