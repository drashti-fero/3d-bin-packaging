<template>
  <v-navigation-drawer
    v-model="drawer"
    expand-on-hover
    :mini-variant="true"
    :clipped="true"
    fixed
    app
    dark
    color="primary"
    v-bind="$attrs"
    width="335px"
    class="app-nav-shadow Scrollbar"
  >
    <v-list dense shaped class="pr-1 pt-2">
      <v-list-item v-for="(link, i) in baseNav" :key="i" class="pa-0">
        <v-list-item-group
          v-if="!link.subLinks"
          v-model="selectedItem"
          class="Full-Width"
          color="white"
        >
          <v-list-item :exact="!!link.exact" router :to="link.to">
            <v-list-item-action>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ link.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>

        <v-list-group v-else class="py-1 Full-Width" color="white">
          <template v-slot:activator>
            <v-list-item-action>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ link.title }}</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="(subLink, i) in link.subLinks"
            router
            exact
            :key="i"
            :to="subLink.to"
          >
            <v-list-item-action>
              <v-icon>{{ subLink.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content class="pl-6">
              <v-list-item-title>{{ subLink.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>


<script>
export default {
  props: {
    value: Boolean,
  },
  data() {
    return {
      selectedItem: 0,
      baseNav: [
        {
          icon: "mdi-alpha-i-circle",
          title: "Items",
          to: "/",
          exact: true,
        },
        {
          icon: "mdi-square",
          title: "Boxes",
          to: `/boxes/`,
          exact: true,
        },
        {
          icon: "mdi-format-quote-close",
          title: "Capacity Quotation",
          to: `/capacity-quotation/`,
          exact: true,
        },
      ],
    };
  },
  computed: {
    drawer: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
};
</script>

<style scoped >
.Full-Width {
  width: 100%;
}
</style>
