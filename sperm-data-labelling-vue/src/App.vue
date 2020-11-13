<template>
  <v-app light>
    <v-navigation-drawer v-if="logged" v-model="drawer" app>
      <v-list>
        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">
              {{ username }}
            </v-list-item-title>
            <v-list-item-subtitle>UserID : {{ userid }}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-icon>mdi-menu-down</v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item-group v-model="item" color="primary">
          <v-list-item v-for="(item, i) in items" :key="i" :to="item.to">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <!--      <v-btn    v-bind="size"-->
      <!--                @click="logout">-->
      <!--        <v-icon left v-bind="size" >mdi-export</v-icon>-->
      <!--        Logout-->

      <!--      </v-btn>-->
      <template v-slot:append>
        <div class="pa-2">
          <v-btn block v-bind="size" @click="logout">
            <v-icon left v-bind="size">mdi-export</v-icon>
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-btn icon x-large @click="home">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-toolbar-title>{{ title }}</v-toolbar-title>

<!--      <v-spacer></v-spacer>-->
<!--      <v-toolbar-title>{{ subtitle }}</v-toolbar-title>-->

      <v-spacer></v-spacer>

      <v-btn v-bind="size" v-if="get_user != null" @click="logout">
        <v-icon left v-bind="size">mdi-export</v-icon>
        Logout
      </v-btn>
    </v-app-bar>

    <v-main class="section-wrapper">
      <!--<transition :name="transitionName">-->

      <!--<transition name="router-anim" enter-active-class="animated fadeInDown" leave-active-class="animated fadeOutDown">-->
      <transition name="router-anim">
        <!--<transition name="page" mode="out-in">-->

        <router-view> </router-view>
      </transition>
    </v-main>

    <AppFooter />
    <!--<div id="nav">-->
    <!--<router-link to="/">Home</router-link> |-->
    <!--<router-link to="/about">About</router-link>-->
    <!--</div>-->
  </v-app>
</template>

<script>
// @ is an alias to /src
import AppFooter from "@/AppFooter";
import store from "./store";
import Cookies from "js-cookie";

export default {
  name: "App",
  components: {
    AppFooter
    // Header
  },
  computed: {
    get_user() {
      return [store.state.userid, store.state.username];
    },
    size() {
      const size = { xs: "small", sm: "small", lg: "large", xl: "x-large" }[
        this.$vuetify.breakpoint.name
      ];
      return size ? { [size]: true } : {};
    }
  },
  created() {
    console.log("App Created");
    this.username = store.state.username;
    this.userid = store.state.userid;

    // console.log("Username: ", this.username);
    // console.log("userid: ", this.userid);
    this.$router.push({ path: "/login" });
  },
  data() {
    return {
      username: null,
      userid: null,
      logged: false,
      item: 0,
      items: [
        { text: "Slides", icon: "mdi-folder", to: "/slides" }
        // { text: "Shared with me", icon: "mdi-account-multiple" },
        // { text: "Starred", icon: "mdi-star" },
        // { text: "Recent", icon: "mdi-history" },
        // { text: "Offline", icon: "mdi-check-circle" },
        // { text: "Uploads", icon: "mdi-upload" },
        // { text: "Backups", icon: "mdi-cloud-upload" }
      ],
      clipped: false,
      drawer: false,
      fixed: false,

      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Image Annotator",
      subtitle: "Home",
      transitionName: "slide-left"
    };
  },
  // beforeRouteUpdate (to, from, next) {
  //   const toDepth = to.path.split('/').length
  //   const fromDepth = from.path.split('/').length
  //   this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
  //   next()
  // },
  methods: {
    logout: function() {
      Cookies.remove("logged_in");
      Cookies.remove("username");
      Cookies.remove("userid");

      store.commit("store_user", null);
      store.commit("store_userid", null);
      this.$router.push({ path: "/login" });
    },
    home: function() {
      this.$router.push({ path: "/slides" });
    }
  },

  watch: {
    $route(to, from) {
      const toDepth = to.path.split("/").length;
      const fromDepth = from.path.split("/").length;
      this.transitionName = toDepth < fromDepth ? "slide-right" : "slide-left";
    },
    get_user: function(newname) {
      this.userid = newname[0];
      this.username = newname[1];
      if (newname != null) this.logged = true;
      else false;
    }
  }
};
</script>

<style>
/*@import './assets/css/custom.css';*/
@media (max-width: 425px) {
  .temp {
    flex-direction: column;
  }

  .image {
    /* object-fit: cover; */
    /* max-height: 60vh; */
    /* height: 30px; */
    /* width: 30px; */
    /* width: 100v÷w; */
  }
}

a {
  text-decoration: none;
}

.page-enter-active,
.page-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}
.page-enter,
.page-leave-to {
  opacity: 0;
  /*transform: translateX(-30%);*/
}

.router-anim-enter-active {
  animation: coming 0.5s;
  animation-delay: 1s;
  opacity: 0;
}
.router-anim-leave-active {
  animation: going 0.2s;
}

@keyframes going {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(100px);
    opacity: 0;
  }
}
@keyframes coming {
  from {
    transform: translateX(-0px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
</style>
