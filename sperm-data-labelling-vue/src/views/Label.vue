<template>
  <v-container>
    <v-layout class="temp" row >
      <v-flex md6 sm6 xs12>
        <img
          v-if="batch_completed"
          class="image"
          src="@/assets/slide_completed.png"
          :aspect-ratio="1"
          alt=""
        />
        <!--        </img>-->
        <img
          v-if="everything_completed"
          class="image"
          src="@/assets/slide_completed.png"
          :aspect-ratio="1"
          alt=""
          style="width:100%"
        />
        <!--        </img>-->
        <img
          v-if="not_completed"
          class="image"
          :src="sperm_image"
          alt=""
          contain
          :style="`transform: rotate(${rotation}deg);`"
        />
        <!--        </img>-->

        <!--{{slide_id}}-->
        <!--{{user_id}}-->
      </v-flex>
      <v-flex md6 sm6 xs12 class="ann_class">
        <!--<v-layout align-space-around justify-space-around  row fill-height fill-width wrap>-->
        <!--<v-flex md12 xs4>-->
        <!--<v-btn color="success">Normal</v-btn>-->
        <!--</v-flex>-->
        <!--<v-flex md12 xs4>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--</v-flex>-->
        <!--<v-flex md12 xs4>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--</v-flex>-->

        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-btn color="success">Success</v-btn>-->
        <!--<v-layout align-space-around justify-space-around  row fill-height fill-width>-->
        <!--<v-btn color="success">Previous</v-btn>-->
        <!--<v-btn color="success">Mark</v-btn>-->
        <!--<v-btn color="success">Next</v-btn>-->
        <!--</v-layout>-->

        <!--</v-layout>-->

        <!--        <v-item-group>-->
        <!--          <v-container grid-list-md>-->
        <!--            <v-layout wrap>-->
        <!--              <v-flex v-for="n in 6" :key="n" xs6 sm12 md12>-->
        <!--                <v-item>-->
        <!--                  &lt;!&ndash;                  <v-card&ndash;&gt;-->
        <!--                  &lt;!&ndash;                    class="d-flex align-center card-custom"&ndash;&gt;-->
        <!--                  &lt;!&ndash;                    light&ndash;&gt;-->
        <!--                  &lt;!&ndash;                    @click="give_label(n)"&ndash;&gt;-->
        <!--                  &lt;!&ndash;                  >&ndash;&gt;-->
        <!--                  &lt;!&ndash;                    <div width="100%" height="100%" style="text-align:center">&ndash;&gt;-->
        <!--                  &lt;!&ndash;                      {{ Active[n] }}&ndash;&gt;-->
        <!--                  &lt;!&ndash;                    </div>&ndash;&gt;-->
        <!--                  &lt;!&ndash;                  </v-card>&ndash;&gt;-->

        <!--                  <v-card-->
        <!--                    class="d-flex align-center card-custom temp"-->
        <!--                    color="primary"-->
        <!--                    dark-->
        <!--                    @click="give_label(n)"-->
        <!--                  >-->
        <!--                    <v-card-title>-->
        <!--                      <v-list-item class="grow">-->
        <!--                        &lt;!&ndash;                        <v-list-item-avatar color="white">&ndash;&gt;-->
        <!--                        &lt;!&ndash;                          <v-img&ndash;&gt;-->
        <!--                        &lt;!&ndash;                            class="elevation-6"&ndash;&gt;-->
        <!--                        &lt;!&ndash;                            alt=""&ndash;&gt;-->
        <!--                        &lt;!&ndash;                            src="../assets/sperm.png"&ndash;&gt;-->
        <!--                        &lt;!&ndash;                          ></v-img>&ndash;&gt;-->
        <!--                        &lt;!&ndash;                        </v-list-item-avatar>&ndash;&gt;-->

        <!--                        &lt;!&ndash;                    <span class="headline font-weight-bold">{{ n }}</span>&ndash;&gt;-->

        <!--                        <v-card-text class="justify-center font-weight-bold">-->
        <!--                          {{ Active[n] }}-->
        <!--                        </v-card-text>-->
        <!--                      </v-list-item>-->
        <!--                    </v-card-title>-->
        <!--                  </v-card>-->
        <!--                </v-item>-->
        <!--              </v-flex>-->

        <!--            </v-layout>-->
        <!--          </v-container>-->
        <!--        </v-item-group>-->

        <!--        <v-radio-group-->
        <!--          v-model="radios"-->
        <!--          mandatory-->

        <!--        >-->
        <!--          <v-radio-->
        <!--            label="Normal Sperm"-->
        <!--            value="normal_sperm"-->
        <!--          ></v-radio>-->
        <!--          <v-radio-->
        <!--            label="Abnormal Sperm"-->
        <!--            value="abnormal_perm"-->
        <!--          ></v-radio>-->
        <!--        </v-radio-group>-->
        <!--        <v-checkbox-->
        <!--          v-model="proximal_droplets"-->
        <!--          :label="`Proximal Droplets`"-->
        <!--        ></v-checkbox>-->
        <!--        <v-checkbox-->
        <!--          v-model="distal_droplets"-->
        <!--          :label="`Distal Droplets`"-->
        <!--        ></v-checkbox>-->
        <!--        <v-checkbox-->
        <!--          v-model="distal_mid_piece_reflex"-->
        <!--          :label="`Distal Mid-Piece Reflex`"-->
        <!--        ></v-checkbox>-->

        <v-container class="grey lighten-5 pa-3 "  >
          <v-divider></v-divider>
          <v-divider></v-divider>
          <v-row align-content="center" align="center" class="pa-1"  >
            <v-col align="center"  class="pa-1"  offset-md="4">
              <!--              <v-radio-->
              <!--                label="Normal Sperm"-->
              <!--                value="normal_sperm"-->
              <!--              ></v-radio>-->

              <!--              <v-checkbox-->
              <!--                v-model="normal_sperm"-->
              <!--                :label="`Normal Sperm`"-->
              <!--              ></v-checkbox>-->

              <!--              <v-btn-toggle-->
              <!--                v-model="toggle_normal_sperm"-->
              <!--                tile-->
              <!--                color="#1a237e"-->
              <!--                group-->
              <!--              >-->
              <!--                <v-btn large rounded>-->
              <!--                  <b>Normal Sperm </b>-->
              <!--                </v-btn>-->
              <!--              </v-btn-toggle>-->
              <!--              -->

              <v-checkbox
                class="justify-center grey lighten-5"
                v-model="toggle_normal_sperm"
                :label="`Normal Sperm`"
                :value="models[`Normal Sperm`]"
              ></v-checkbox>
            </v-col >
            <!--            <v-col>-->
            <!--              <v-btn-toggle-->
            <!--                v-model="toggle_abnormal_sperm"-->
            <!--                tile-->
            <!--                color="#1a237e"-->
            <!--                group-->
            <!--              >-->
            <!--                <v-btn large rounded>-->
            <!--                  <b>Abnormal Sperm </b>-->
            <!--                </v-btn>-->
            <!--              </v-btn-toggle>-->

            <!--              &lt;!&ndash;              <v-checkbox&ndash;&gt;-->
            <!--              &lt;!&ndash;                v-model="abnormal_sperm"&ndash;&gt;-->
            <!--              &lt;!&ndash;                :label="`Abnormal Sperm`"&ndash;&gt;-->
            <!--              &lt;!&ndash;              ></v-checkbox>&ndash;&gt;-->

            <!--              &lt;!&ndash;              <v-radio&ndash;&gt;-->
            <!--              &lt;!&ndash;                label="Abnormal Sperm"&ndash;&gt;-->
            <!--              &lt;!&ndash;                value="abnormal_sperm"&ndash;&gt;-->
            <!--              &lt;!&ndash;              ></v-radio>&ndash;&gt;-->
            <!--            </v-col>-->
          </v-row>

          <v-divider></v-divider>
          <v-divider></v-divider>

          <v-row   class="pa-0">
            <v-col   class="pa-0"         offset-md="1">
              <v-checkbox
                v-model="check_model"
                :label="`Proximal Droplets`"
                :value="models[`Proximal Droplets`]"
              ></v-checkbox>
            </v-col>

            <v-col   class="pa-0">
              <v-checkbox
                v-model="check_model"
                :label="`Distal Droplets`"
                :value="models[`Distal Droplets`]"
              ></v-checkbox>
            </v-col>
          </v-row>

          <v-row   class="pa-0">
            <v-col   class="pa-0 "  offset-md="1">
              <v-checkbox
                v-model="check_model"
                :label="`Distal Mid-Piece Reflex`"
                :value="models[`Distal Mid-Piece Reflex`]"
              ></v-checkbox>
            </v-col>

            <v-col   class="pa-0">
              <v-checkbox
                v-model="check_model"
                :label="`Clumped Sperm`"
                :value="models[`Clumped Sperm`]"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-divider></v-divider>

          <v-row   class="pa-0">
            <v-col   class="pa-0" offset-md="1">
              <v-list

                align="center"
                class="justify-center grey lighten-5"
                v-for="item in Headitems"
                :key="item.title"
              >
                <!--                <v-list-group-->
                <!--                  v-for="item in Headitems"-->
                <!--                  :key="item.title"-->
                <!--                  class="v-list-group&#45;&#45;active"-->
                <!--                  no-action-->

                <!--                >-->
                <!--            :prepend-icon="item.action"-->

                <!--                  <template v-slot:activator>-->
                <!--                    <v-list-item-content>-->
                <!--                      <v-list-item-title v-text="item.title"></v-list-item-title>-->
                <!--                    </v-list-item-content>-->
                <!--                  </template>-->

                <v-list-item-content class="justify-center">
                  <b>{{ item.title }}</b>

                  <!--                                      <v-list-item-title class="justify-center" v-text="item.title"></v-list-item-title>-->
                </v-list-item-content>

                <v-list-item v-for="child in item.items" :key="child.title">
                  <!--              <v-list-item-content>-->

                  <v-checkbox   class="pa-0"
                    v-model="check_model"
                    :label="child.title"
                    :value="models[child.title]"
                  ></v-checkbox>

                  <!---->
                  <!--              </v-list-item-content>-->
                </v-list-item>
                <!--                </v-list-group>-->
              </v-list>
            </v-col>

            <v-divider vertical></v-divider>
            <v-divider vertical></v-divider>

            <v-col align="center">
              <v-list
                class="justify-center grey lighten-5"
                v-for="item in Tailitems"
                :key="item.title"
              >
                <!--                <v-list-group-->
                <!--                  v-for="item in Tailitems"-->
                <!--                  :key="item.title"-->
                <!--&lt;!&ndash;                  v-model="item.active"&ndash;&gt;-->

                <!--                  no-action-->
                <!--                >-->
                <!--            :prepend-icon="item.action"-->

                <!--                  <template v-slot:activator>-->
                <!--                    <v-list-item-content>-->
                <!--                      <v-list-item-title v-text="item.title"></v-list-item-title>-->
                <!--                    </v-list-item-content>-->
                <!--                  </template>-->

                <v-list-item-content class="justify-center">
                  <b>{{ item.title }}</b>

                  <!--                                      <v-list-item-title class="justify-center" v-text="item.title"></v-list-item-title>-->
                </v-list-item-content>

                <v-list-item
                  align="center"
                  v-for="child in item.items"
                  :key="child.title"
                >
                  <!--              <v-list-item-content>-->

                  <v-checkbox
                    align="center"
                    v-model="check_model"
                    :label="child.title"
                    :value="models[child.title]"
                  ></v-checkbox>

                  <!---->
                  <!--              </v-list-item-content>-->
                </v-list-item>
                <!--                </v-list-group>-->
              </v-list>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-divider></v-divider>

          <v-row  class="pa-1">
            <v-col  class="pa-1" offset-md="4">
              <v-checkbox
                class="pa-1"
                v-model="check_model"
                :label="`Other Abnormalities`"
                :value="models[`Other Abnormalities`]"
              ></v-checkbox>
            </v-col>

          </v-row>

          <v-divider></v-divider>
          <v-divider></v-divider>
          <v-row>
            <v-col align="center">
              <v-btn
                x-large
                class="ma-2"
                :loading="loading"
                :disabled="submit_button_disable"
                color="primary"
                @click="submit()"
              >
                SUBMIT
                <template v-slot:loader>
                  <span class="custom-loader">
                    <v-icon light>mdi-cached</v-icon>
                  </span>
                </template>
              </v-btn>
            </v-col>
          </v-row>
        </v-container>

        <!--        <v-card-->
        <!--          class="d-flex align-center card-custom temp"-->
        <!--          color="primary"-->
        <!--          dark-->
        <!--          @click="submit(n)"-->
        <!--        >-->
        <!--          <v-card-title>-->
        <!--            <v-list-item class="grow">-->
        <!--              &lt;!&ndash;                        <v-list-item-avatar color="white">&ndash;&gt;-->
        <!--              &lt;!&ndash;                          <v-img&ndash;&gt;-->
        <!--              &lt;!&ndash;                            class="elevation-6"&ndash;&gt;-->
        <!--              &lt;!&ndash;                            alt=""&ndash;&gt;-->
        <!--              &lt;!&ndash;                            src="../assets/sperm.png"&ndash;&gt;-->
        <!--              &lt;!&ndash;                          ></v-img>&ndash;&gt;-->
        <!--              &lt;!&ndash;                        </v-list-item-avatar>&ndash;&gt;-->

        <!--              &lt;!&ndash;                    <span class="headline font-weight-bold">{{ n }}</span>&ndash;&gt;-->

        <!--              <v-card-text class="justify-center font-weight-bold">-->
        <!--                Submit-->
        <!--                &lt;!&ndash;                <h3>Submit</h3>&ndash;&gt;-->
        <!--              </v-card-text>-->
        <!--            </v-list-item>-->
        <!--          </v-card-title>-->
        <!--        </v-card>-->
        <!--        {{toggle_normal_sperm}}-->
        <!--        {{toggle_abnormal_sperm}}-->

        <!-- <v-item-group>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex
                v-for="n in 1"
                :key="n"
                xs12
                md12
              >
                <v-item>
                  <v-card class="d-flex align-center card-custom" light
                          @click="toggleon(Active1[n])">
                    <div width=100% height=100% style="text-align:center">
                      {{Active1[n]}}
                    </div>
                  </v-card>
                </v-item>
              </v-flex>
            </v-layout>
          </v-container>
        </v-item-group> -->
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// import * as Buffer from "vuetify";
import store from "@/store";

const axios = require("axios");

export default {
  data: () => ({
    loader: null,
    loading: false,
    toggle_normal_sperm: null,
    // toggle_abnormal_sperm: null,
    submit_button_disable: true,
    toggle_sperm: false,

    cors: "https://cors-anywhere.herokuapp.com/",
    sperm_image: null,

    // Active:["Saab", "Volvo", "BMW","Saab", "Volvo", "BMW","Saab", "Volvo", "BMW","Saab", "Volvo", "BMW", "Audi"],
    // Active:["chuck","Normal Sperm","Abnormal acrosomes","Abnormal heads","Detached heads","Proximal droplets", "Distal droplets","Bent or coiled midpieces", "Other midpiece abnormalities","Hairpin or bent tail","Coiled tails","Other cells","Not sperm/cannot label"],
    models: {
      "Head Abnormalities": "head_abnormalities",
      "Normal Sperm": "normal_sperm",
      "Abnormal Sperm": "abnormal_sperm",
      "Proximal Droplets": "proximal_droplets",
      "Distal Droplets": "distal_droplets",
      "Distal Mid-Piece Reflex": "distal_mid_piece_reflex",
      "Head abnormalities": "head_abnormalities",
      Macrohead: "macrohead",
      Microhead: "microhead",
      "Missing head": "missing_head",
      "Double head": "double_head",
      "Tail Abnormalities": "tail_abnormalities",
      "Coiled tail": "coiled_tail",
      "Missing tail": "missing_tail",
      "Bent tail": "bent_tail",
      "Clumped Sperm": "clumped_sperm",
      "Other Abnormalities": "other_abnormalities"
    },

    check_model: [],
    Active: [
      "chuck",
      "Normal Sperm",
      // "Abnormal acrosomes",
      // "Abnormal heads",
      // "Detached heads",
      // "Proximal droplets",
      // "Distal droplets",
      // "Bent or coiled midpieces",
      // "Other midpiece abnormalities",
      // "Hairpin or bent tail",
      "Head Defect",
      "Neck Defect",
      "Tail Defect",
      "Other Defects",
      "Other cells",
      "Not sperm/cannot label"
    ],
    label: "",
    imageno: "",
    // slide: "",
    image_name: "",
    slide_id: "",
    user_id: "",
    batch_completed: false,
    everything_completed: false,
    not_completed: false,
    rotation: 0,

    Headitems: [
      {
        action: "mdi-ticket",
        items: [
          { title: "Macrohead" },
          { title: "Microhead" },
          { title: "Missing head" },
          { title: "Double head" }
        ],
        title: "Head Abnormalities"
      }
    ],
    Tailitems: [
      {
        action: "mdi-ticket",
        items: [
          { title: "Coiled tail" },
          { title: "Missing tail" },
          { title: "Bent tail" }
        ],
        title: "Tail Abnormalities"
      }
    ]
  }),

  watch: {
    toggle_normal_sperm: function() {
      // console.log(this.toggle_normal_sperm);
      if (this.toggle_normal_sperm === "normal_sperm") {
        this.check_model = [];
      }

      this.submit_button_disable =
        this.toggle_normal_sperm === null && this.check_model.length === 0;
    },
    // toggle_abnormal_sperm: function() {
    //   if (this.toggle_abnormal_sperm === 0) {
    //     this.toggle_normal_sperm = null;
    //   }
    //
    //   this.submit_button_disable =
    //     this.toggle_normal_sperm === null &&
    //     this.toggle_abnormal_sperm === null;
    // },
    image_name: function() {
      if (this.image_name) this.get_image();
    },

    check_model: function() {
      // console.log(
      //   this.check_model,
      //   // this.toggle_abnormal_sperm,
      //   this.toggle_normal_sperm
      // );
      if (this.check_model.length !== 0) {
        this.toggle_normal_sperm = null;
        // this.toggle_abnormal_sperm = 0;
      }
      // else {
      //   this.toggle_normal_sperm = 'normal_sperm';
      //   // this.toggle_abnormal_sperm = null;
      // }

      this.submit_button_disable =
        this.toggle_normal_sperm === null && this.check_model.length === 0;
    },

    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    }
  },
  computed: {
    get_user() {
      return store.state.userid;
    },

    size() {
      const size = { xs: "small", sm: "small", lg: "large", xl: "x-large" }[
        this.$vuetify.breakpoint.name
      ];
      return size ? { [size]: true } : {};
    }
  },

  created() {
    // this.check_model  =  [];
    // console.log("created " + this.toggle_normal_sperm + this.check_model)

    this.slide_id = store.state.current_slide;
    this.userid = store.state.userid;
    this.username = store.state.username;
    this.image_name = this.getimagenumber();

    // console.log("Username: ", this.username);
    // console.log("userid: ", this.userid);
    // console.log("image_name: ", this.image_name);
    // console.log("slide_id: ", this.slide_id);

    // console.log("size: ", this.$vuetify.breakpoint.name);

    if (
      this.$vuetify.breakpoint.name === "xs" ||
      this.$vuetify.breakpoint.name === "sm"
    ) {
      this.rotation -= 0;
    }
    this.submit_button_disable =
      this.toggle_normal_sperm === null && this.check_model.length === 0;

    // this.reset_ann()
  },
  rotateRight() {},
  methods: {
    get_model: function(name) {
      return name.toLowerCase().replace(" ", "_");
    },

    reset_ann: function() {
      this.toggle_normal_sperm = null;
      this.check_model = [];
    },
    submit: function() {
      this.loader = "loading";
      this.loading = !this.submit_button_disable;
      let label;
      if (this.toggle_normal_sperm === "normal_sperm") {
        label = "normal_sperm";
      } else {
        label = this.check_model.toString();
      }
      // console.log(label);

      let data = {
        username: this.userid,
        image_name: this.image_name,
        label: label,
        comment: ""
      };

      const get_label = this.$backendhostname + "/give_label";

      axios
        .post(get_label, data, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Origin, X-Requested-With, Content-Type, Accept"
          }
        })

        .then(response => {
          if (response.data.response) {
            // console.log("success");
            this.sperm_image = "";
            this.image_name = this.getimagenumber();
            this.reset_ann();
          }

          // var res = response.data.user

          // dispatch({type: FOUND_USER, data: response.data[0]})
        })
        .catch(error => {
          this.resp = error;
          console.error(error);

          // dispatch({type: ERROR_FINDING_USER})
        });
    },

    give_label: function(temp) {
      // console.log(temp);

      let data = {
        username: this.userid,
        image_name: this.image_name,
        label: temp - 1,
        comment: ""
      };

      const get_label = this.$backendhostname + "/give_label";

      axios
        .post(get_label, data, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Origin, X-Requested-With, Content-Type, Accept"
          }
        })

        .then(response => {
          if (response.data.response) {
            // console.log("success");
            this.sperm_image = "";
            this.image_name = this.getimagenumber();
          }
          // var res = response.data.user

          // dispatch({type: FOUND_USER, data: response.data[0]})
        })
        .catch(error => {
          this.resp = error;
          console.error(error);

          // dispatch({type: ERROR_FINDING_USER})
        });
    },
    getimagenumber: function() {
      // console.log(this.user_id);
      let data = {
        username: this.userid,
        slide: this.slide_id
      };

      const get_image_number_url = this.$backendhostname + "/get_image_number";

      // this.$route.params

      axios
        .post(get_image_number_url, data, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Origin, X-Requested-With, Content-Type, Accept"
          }
        })

        .then(response => {
          if (response.data.response === "success") {
            // console.log("success");
            this.not_completed = true;
            this.batch_completed = false;
            this.everything_completed = false;

            this.image_name = response.data.image_name;
            return response.data.image_name;
          } else if (response.data.response === "slide_completed") {
            this.not_completed = false;

            this.batch_completed = true;
            this.everything_completed = false;
          } else if (response.data.response === "completed") {
            this.batch_completed = false;
            this.not_completed = false;
            this.everything_completed = true;
          }
          // var res = response.data.user

          // dispatch({type: FOUND_USER, data: response.data[0]})
        })
        .catch(error => {
          this.resp = error;
          console.error(error);

          // dispatch({type: ERROR_FINDING_USER})
        });
    },

    get_image: function() {
      // console.log(this.user_id);
      let data = {
        image_name: this.image_name
      };

      // let data1 = {"image_name":"Ash11_0021_955_930.png"}

      const get_image_url = this.$backendhostname + "/get_image";

      // this.$route.params

      // this.sperm_image = axios.post(this.cors+get_image_url, data1, {headers: {
      //     'Content-Type': 'application/json','Access-Control-Allow-Origin': '*',
      //     'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
      //
      //   }})
      //   .then(response => `data:${response.headers['content-type']};base64,${btoa(String.fromCharCode(...new Uint8Array(response.data)))}`).catch((error) => {
      //     this.resp= error
      //     console.error(error)
      //
      //     // dispatch({type: ERROR_FINDING_USER})
      //   });

      axios
        .post(get_image_url, data, {
          responseType: "arraybuffer",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Origin, X-Requested-With, Content-Type, Accept"
          }
        })

        .then(response => {
          this.sperm_image = this._imageEncode(response.data);
        })
        .catch(error => {
          this.resp = error;
          console.error(error);
        });
    },

    _imageEncode: function(arrayBuffer) {
      // let u8 = new Uint8Array(arrayBuffer);
      let b64encoded = btoa(
        [].reduce.call(
          new Uint8Array(arrayBuffer),
          function(p, c) {
            return p + String.fromCharCode(c);
          },
          ""
        )
      );
      let mimetype = "image/png";
      return "data:" + mimetype + ";base64," + b64encoded;
    }
  }
};
</script>

<style>
.temp{
  display: flex;
  height: 100%;


}
.theme--light.v-divider {
  border-color: rgba(0, 0, 0, 1) !important;
}

.card-custom {
  flex-direction: column;

  /*height: 100px;*/
}
.ann_class{
  /*max-height: 100vh;*/
}
.image {
  height: 100%;
  display: block;
  margin: 0 auto;
  /* object-fit: cover; */
   max-height: 80vh;
  /* height: 30px; */
  /* width: 30px; */
  /* width: 100v÷w; */
}
/*@media (max-width: 500px) {*/
/*  .temp {*/
/*    flex-direction: column;*/
/*  }*/
/*  .card-custom {*/
/*    !*height: 10px;*!*/
/*  }*/
/*}*/
/*@media (min-width: 960px) {*/
/*  .temp {*/
/*    !*flex-direction: column;*!*/
/*  }*/
/*  .card-custom {*/
/*    !*height: 10px;*!*/
/*  }*/

/*  .image {*/
/*    !* object-fit: cover; *!*/
/*    !* max-height: 60vh; *!*/
/*    !* height: 30px; *!*/
/*    !* width: 30px; *!*/
/*    !* width: 100v÷w; *!*/
/*    height: 100%;*/
/*    display: block;*/
/*    margin: 0 auto;*/
/*  }*/
/*}*/
/*@media (max-width: 960px) {*/
/*  .temp {*/
/*    !*flex-direction: column;*!*/
/*  }*/
/*  .card-custom {*/
/*    !*height: 10px;*!*/
/*  }*/

/*  .image {*/
/*    !* object-fit: cover; *!*/
/*    !* max-height: 60vh; *!*/
/*    !* height: 30px; *!*/
/*    !* width: 30px; *!*/
/*    !* width: 100v÷w; *!*/
/*    !*width: 30%;*!*/
/*    !*height: 100%;*!*/

/*  }*/
/*}*/

/* default styles here for older browsers.
   I tend to go for a 600px - 960px width max but using percentages
*/
/*@media only screen and (min-width: 960px) {*/
/*  !* styles for browsers larger than 960px; *!*/
/*  .image {*/
/*    height: 100%;*/
/*  }*/
/*}*/
/*@media only screen and (min-width: 1440px) {*/
/*  !* styles for browsers larger than 1440px; *!*/
/*  !* styles for browsers larger than 960px; *!*/
/*  .image {*/
/*    height: 100%;*/
/*  }*/
/*}*/
/*@media only screen and (min-width: 2000px) {*/
/*  !* for sumo sized (mac) screens *!*/

/*  !* styles for browsers larger than 960px; *!*/
/*  .image {*/
/*    height: 100%;*/
/*  }*/
/*}*/
/*@media only screen and (max-device-width: 480px) {*/
/*  !* styles for mobile browsers smaller than 480px; (iPhone) *!*/
/*  .temp {*/
/*    flex-direction: column;*/
/*  }*/
/*  .card-custom {*/
/*    !*height: 10px;*!*/
/*  }*/
/*}*/
/*@media only screen and (device-width: 768px) {*/
/*  !* default iPad screens *!*/
/*  .temp {*/
/*    flex-direction: column;*/
/*  }*/
/*  .card-custom {*/
/*    !*height: 10px;*!*/
/*  }*/
/*  .image {*/
/*    width: 100%;*/

/*    display: block;*/
/*    margin: 0 auto;*/
/*  }*/
/*}*/
/*!* different techniques for iPad screening *!*/
/*@media only screen and (min-device-width: 481px) and (max-device-width: 1024px) and (orientation: portrait) {*/
/*  !* For portrait layouts only *!*/
/*}*/

/*@media only screen and (min-device-width: 481px) and (max-device-width: 1024px) and (orientation: landscape) {*/
/*  !* For landscape layouts only *!*/
/*}*/

/*       */

.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
