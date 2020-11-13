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
                    label="User Name"
                    type="text"
                    hint="Your Name"
                    persistent-hint
                    outlined
                  ></v-text-field>
                  <v-text-field
                    prepend-icon="person"
                    name="login"
                    v-model="userid"
                    label="User ID"
                    type="text"
                    hint="You will use to login. Please save this!"
                    persistent-hint
                    outlined
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    prepend-icon="lock"
                    v-model="password"
                    name="password"
                    label="Password"
                    type="password"
                    hint="You will use to login. Please save this!"
                    persistent-hint
                    outlined
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
  </v-app>
</template>

<script>
// import { url } from "@/variables";

const axios = require("axios");

export default {
  data: () => ({
    drawer: null,
    username: "",
    userid: "",
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
      this.$router.push({ path: `/login` }); // -> /user/123
    },
    postPost: function() {
      let data = {
        usernameact: this.username,
        username: this.userid,
        password: this.password
      };
      axios
        // .post("https://cors-anywhere.herokuapp.com/" + url + "/login", data, {
        .post(this.$backendhostname + "/register", data, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Origin, X-Requested-With, Content-Type, Accept"
          }
        })

        .then(response => {
          this.resp = response.data.user;
          // var res = response.data.user;
          // var res = data.username;

          console.log(response.data);
          this.loading = false;
          console.log("Loading state");
          if (response.data.response === "success") {
            console.log(this.loading);
            // this.$router.push({ name: 'user',params : { res} }) // -> /user/123
            // this.$router.push({ path: `/slide/${res}` }); // -> /user/123
            this.$router.push({ path: `/login` }); // -> /user/123
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
