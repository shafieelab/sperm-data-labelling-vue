<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Signup form</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <!-- <template v-slot:activator="{ on }">
                    <v-btn :href="source" icon large target="_blank" v-on="on">
                      <v-icon large>code</v-icon>
                    </v-btn>
                  </template> -->
                  <span>Source</span>
                </v-tooltip>
                <!-- <v-tooltip right>
                  <template v-slot:activator="{ on }">
                    <v-btn icon large href="https://codepen.io/johnjleider/pen/wyYVVj" target="_blank" v-on="on">
                      <v-icon large>mdi-codepen</v-icon>
                    </v-btn>
                  </template>
                  <span>Codepen</span>
                </v-tooltip> -->
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field
                    prepend-icon="person"
                    name="login"
                    v-model="username"
                    label="Login"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    prepend-icon="lock"
                    v-model="password"
                    name="password"
                    label="Password"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="postPost" color="primary">Signup</v-btn>
                <v-btn @click="postPost1" color="primary"
                  >Go to login page</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
const axios = require("axios");

export default {
  data: () => ({
    drawer: null,
    username: "",
    password: "",
    resp: ""
  }),
  props: {
    source: String
  },
  methods: {
    postPost1: function() {
      this.$router.push({ path: `/login` }); // -> /user/123
    },
    postPost: function() {
      let data = {
        username: this.username,
        password: this.password
      };
      axios
        .post(
          "https://cors-anywhere.herokuapp.com/https://shafieelabdatalabeling.tk/register",
          data,
          {
            headers: {
              "Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Headers":
                "Origin, X-Requested-With, Content-Type, Accept"
            }
          }
        )

        .then(response => {
          console.log(response.data.user);
          // this.$router.push({ name: 'user',params : { res} }) // -> /user/123
          this.$router.push({ path: `/login` }); // -> /user/123

          // dispatch({type: FOUND_USER, data: response.data[0]})
        })
        .catch(error => {
          this.resp = error;
          console.error(error);

          // dispatch({type: ERROR_FINDING_USER})
        });
    }
  }
};
</script>
