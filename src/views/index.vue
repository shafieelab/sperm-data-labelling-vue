<template>
  <v-layout column justify-center align-center>
    <v-flex>
      Hello World!!!
    </v-flex>
  </v-layout>
</template>

<script>
// import Logo from "~/components/Logo.vue";
// import VuetifyLogo from "~/components/VuetifyLogo.vue";

export default {
  // components: {
  //   Logo,
  //   VuetifyLogo
  // },

  created() {
    this.$router.push({ path: `/login` }); // -> /user/123
  }
};
</script>
