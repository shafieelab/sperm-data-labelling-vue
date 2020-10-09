<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login form</v-toolbar-title>
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
                <v-btn @click="postPost" color="primary">Login</v-btn>

                <v-btn @click="postPost1" color="primary"
                  >Go to signup page</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>

      <v-snackbar
        v-model="snackbar"
        :bottom="y === 'bottom'"
        :left="x === 'left'"
        :multi-line="mode === 'multi-line'"
        :right="x === 'right'"
        :timeout="timeout"
        :top="y === 'top'"
        :vertical="mode === 'vertical'"
      >
        {{ text }}
        <v-btn color="pink" flat @click="snackbar = false">
          Close
        </v-btn>
      </v-snackbar>
    </v-content>
    <span v-if="!loading" class="Button__Content">
      <slot></slot>
    </span>
  </v-app>
</template>

<script>
const axios = require("axios");

export default {
  data: () => ({
    drawer: null,
    username: "",
    password: "",
    resp: "",
    loading: { type: Boolean, default: false },
    snackbar: false,
    y: "top",
    x: null,
    mode: "",
    timeout: 6000,
    text: "Username or Password is Invalid, Please try again."
  }),
  props: {
    source: String
  },
  methods: {
    postPost1: function() {
      this.$router.push({ path: `/signup` }); // -> /user/123
    },

    postPost: function() {
      this.loading = true;
      console.log("Loading state");
      console.log(this.loading);
      let data = {
        username: this.username,
        password: this.password
      };
      axios
        .post(
          "https://cors-anywhere.herokuapp.com/https://shafieelabdatalabeling.tk/login",
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
          this.resp = response.data.user;
          var res = response.data.user;

          console.log(response.data);
          this.loading = false;
          console.log("Loading state");
          if (response.data.response === "success") {
            console.log(this.loading);
            // this.$router.push({ name: 'user',params : { res} }) // -> /user/123
            this.$router.push({ path: `/slide/${res}` }); // -> /user/123
          }
          // this.$router.push({ path: 'user', query: { plan: 'private' } })
          else {
            this.text = response.data.error;
            this.snackbar = true;
            // this.$router.push({path: '/signup'})
          }

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
