import Vue from "vue";
import Vuex from "vuex";
// import VuexPersistence from "vuex-persist";
// const axios = require("axios");
// const vuexLocal = new VuexPersistence({
//   storage: window.localStorage
// })
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userid: null,
    username: null,
    current_slide: null,
    logged_in: false
  },
  mutations: {
    store_user(state, username) {
      // state.idToken = userData.token;
      state.username = username;
    },
    store_userid(state, userid) {
      // state.idToken = userData.token;
      state.userid = userid;
    },
    store_current_slide(state, slide) {
      // state.idToken = userData.token;
      state.current_slide = slide;
    },
    logged_in(state, value) {
      state.logged_in = value;
    }
  },
  actions: {
    // login ({commit}, authData) {
    //
    //   axios
    //     // .post("https://cors-anywhere.herokuapp.com/" + url + "/login", data, {
    //     .post("http://127.0.0.1:5000/login", data, {
    //       headers: {
    //         "Content-Type": "application/json",
    //         "Access-Control-Allow-Origin": "*",
    //         "Access-Control-Allow-Headers":
    //           "Origin, X-Requested-With, Content-Type, Accept"
    //       }
    //     })
    //
    //
    //
    //
    //   axios.post('/verifyPassword?key=[add your Firebase API key here]',{
    //     email: authData.email,
    //     password: authData.password,
    //     returnSecureToken: truen      })
    //     .then(res => {
    //       console.log(res)
    //     })
    //     .catch(error => console.log(error))
    // },
  },

  getters: {
    // doneTodos: state => {
    //   return state.todos.filter(todo => todo.done);
    // }
  },
  modules: {}
  // plugins: [vuexLocal.plugin]
});
