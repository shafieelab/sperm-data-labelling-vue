<template>
  <v-container>
    <v-layout class="temp" row wrap>
      <v-flex md12 xs12>
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

        <v-item-group>
          <v-container grid-list-md>
            <v-layout wrap>
              <!--{{$route.params.id}}-->

              <v-flex v-for="n in Active" :key="n" xs12 sm6 md3 lg3>
                <v-item>
                  <v-hover open-delay="200">
                    <v-card
                      class="d-flex align-center card-custom"
                      color="primary"
                      dark
                      @click="give_label(n)"
                    >
                      <!--                            <div width="100%" height="100%" style="text-align:center">-->
                      <!--                              {{ n }}-->
                      <!--                            </div>-->
                      <v-card-title>
                        <v-list-item class="grow">
                          <v-list-item-avatar color="white">
                            <v-img
                              contain
                              v-bind="size"
                              class="elevation-6"
                              alt=""
                              src="../assets/sperm.png"
                            ></v-img>
                          </v-list-item-avatar>

                          <!--                    <span class="headline font-weight-bold">{{ n }}</span>-->

                          <v-card-text class=" justify-center font-weight-bold">
                            {{ n }}
                          </v-card-text>
                        </v-list-item>
                      </v-card-title>

                      <!--                            <v-card-text-->
                      <!--                              class=" justify-center font-weight-bold"-->
                      <!--                            >-->
                      <!--                              {{ n }}-->
                      <!--                            </v-card-text>-->
                    </v-card>
                  </v-hover>
                </v-item>
              </v-flex>
            </v-layout>
          </v-container>
        </v-item-group>
      </v-flex>

      <!--      <v-main>-->
      <!--        <v-container>-->
      <!--          <v-row>-->
      <!--            <v-col v-for="n in Active" :key="n" cols="4" @click="give_label(n)">-->
      <!--              <v-card class="mx-auto card-custom" color="#26c6da" dark>-->
      <!--                <v-card-title>-->
      <!--                  <v-list-item class="grow">-->
      <!--&lt;!&ndash;                    <v-list-item-avatar color="white">&ndash;&gt;-->
      <!--&lt;!&ndash;                      <v-img&ndash;&gt;-->
      <!--&lt;!&ndash;                        class="elevation-6"&ndash;&gt;-->
      <!--&lt;!&ndash;                        alt=""&ndash;&gt;-->
      <!--&lt;!&ndash;                        src="../assets/sperm.png"&ndash;&gt;-->
      <!--&lt;!&ndash;                      ></v-img>&ndash;&gt;-->
      <!--&lt;!&ndash;                    </v-list-item-avatar>&ndash;&gt;-->

      <!--                    &lt;!&ndash;                    <span class="headline font-weight-bold">{{ n }}</span>&ndash;&gt;-->

      <!--                    <v-card-text-->
      <!--                      class=" justify-center font-weight-bold"-->
      <!--                    >-->
      <!--                      {{ n }}-->
      <!--                    </v-card-text>-->
      <!--                  </v-list-item>-->
      <!--                </v-card-title>-->
      <!--              </v-card>-->
      <!--            </v-col>-->
      <!--          </v-row>-->
      <!--        </v-container>-->
      <!--      </v-main>-->
    </v-layout>
  </v-container>
</template>

<script>
// import * as Buffer from "vuetify";

const axios = require("axios");
import store from "../store";

export default {
  data: () => ({
    cors: "https://cors-anywhere.herokuapp.com/",
    sperm_image: null,
    // username: "",
    userid: "",
    Active: [],
    label: "",
    imageno: "",
    // slide: "",
    image_name: "",
    current_slide: ""
  }),
  computed: {
    size() {
      const size = { xs: "x-small", sm: "small", lg: "large", xl: "x-large" }[
        this.$vuetify.breakpoint.name
      ];
      return size ? { [size]: true } : {};
    },
    get_user() {
      return store.state.userid;
    }
  },
  watch: {},

  created() {
    // this.$parent.subtitle = "Slides";
    // console.log("Created");
    this.give_slides();
    this.userid = store.state.userid;

    // console.log("userid: ", this.userid);
    if (this.userid == null) {
      this.$router.push({ path: "/login" });
    }
  },
  methods: {
    give_slides: function() {
      const get_sli = this.$backendhostname + "/getslides";
      axios
        // .post(this.cors + get_sli, {
        .post(get_sli, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Origin, X-Requested-With, Content-Type, Accept"
          }
        })

        .then(response => {
          // console.log(response);
          this.Active = response.data.slides.split(";");
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
      this.current_slide = temp;
      store.commit("store_current_slide", this.current_slide);

      this.$router.push({
        // path: `/slide/${this.current_slide}/${this.username}`

        path: "/label"
      });
    }
  }
};
</script>

<style>
.card-custom {
  align-content: center;

  /*height: 100px;*/
}
/*@media (max-width: 425px) {*/
/*  .temp {*/
/*    flex-direction: row;*/
/*  }*/
/*  .card-custom {*/
/*    !*height: 100px;*!*/
/*    align-content: center;*/
/*    !*width: 200px;*!*/
/*  }*/

/*  .image {*/
/*    !* object-fit: cover; *!*/
/*    !* max-height: 60vh; *!*/
/*    !* height: 30px; *!*/
/*    !* width: 30px; *!*/
/*    !* width: 100v÷w; *!*/
/*  }*/
/*}*/
.image {
  /* object-fit: cover; */
  /* max-height: 60vh; */
  /* height: 80vh; */
  /* width: 80vh; */
  /* width: 100v÷w; */
}
</style>
<style lang="sass" scoped>
.v-card.on-hover.theme--dark
  background-color: rgba(#FFF, 0.8)
  >.v-card__text
    color: #000
</style>
