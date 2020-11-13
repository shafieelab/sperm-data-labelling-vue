import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import vuetify from "./plugins/vuetify";
import "material-design-icons-iconfont/dist/material-design-icons.css"; // Ensure you are using css-loader
import * as update from "./update";

import axios from "axios";
axios.interceptors.response.use(response => {
  update.update_from_cookies();
  return response;
});
update.check_status();
// if (!logged_in) this.$router.push({ path: "/login" });
// Vue.prototype.$hostname = 'http://localhost:3000'

Vue.config.productionTip = true;
Vue.prototype.$backendhostname = (Vue.config.productionTip) ? 'https://backend.annotator.shafieelab.org' : 'http://localhost:5000'


axios
  // .post("https://cors-anywhere.herokuapp.com/" + url + "/login", data, {
  .get(Vue.prototype.$backendhostname + "/index",  {
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers":
        "Origin, X-Requested-With, Content-Type, Accept"
    }
  })


const app = new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
  // ,
  // created () {
  //   if (sessionStorage.redirect) {
  //     const redirect = sessionStorage.redirect
  //     delete sessionStorage.redirect
  //     this.$router.push(redirect)
  //   }
  // }
});

app.$mount("#app");
