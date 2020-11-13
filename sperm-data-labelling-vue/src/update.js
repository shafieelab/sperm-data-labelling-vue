import Cookie from "js-cookie";
import store from "./store";

export function update_from_cookies() {
  let logged_in = Cookie.get("logged_in");
  if (logged_in && JSON.parse(logged_in)) {
    store.commit("logged_in", true);
    let username = Cookie.get("username");
    let userid = Cookie.get("userid");
    store.commit("store_user", username);
    store.commit("store_userid", userid);
    // console.log("In Update js");
    // console.log("Already logged in");
    // console.log("username", username);
    // console.log("userid", userid);
    // console.log("logged_in", logged_in);
  } else {
    store.commit("logged_in", false);
    // console.log("In Update js");
    // console.log("not logged in");
    // console.log("logged_in", logged_in);
  }
}

export function check_status(){




}
