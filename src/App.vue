<template>
  <div id="app">
    <div>
      <Header msg="Welcome to Shafiee Lab Annotator" />
    </div>
    <div>
      <main class="section-wrapper">
        <!--<transition :name="transitionName">-->

        <!--<transition name="router-anim" enter-active-class="animated fadeInDown" leave-active-class="animated fadeOutDown">-->
        <transition name="router-anim">
          <!--<transition name="page" mode="out-in">-->

          <router-view> </router-view>
        </transition>
      </main>
    </div>

    <!--    <AppFooter />-->
    <!--<div id="nav">-->
    <!--<router-link to="/">Home</router-link> |-->
    <!--<router-link to="/about">About</router-link>-->
    <!--</div>-->
  </div>
</template>

<script>
// @ is an alias to /src
// import Header from "./components/Header";
// import AppFooter from "@/AppFooter";

export default {
  name: "App",
  components: {
    // AppFooter,
    // Header
  },
  data() {
    return {
      transitionName: "slide-left"
    };
  },
  // beforeRouteUpdate (to, from, next) {
  //   const toDepth = to.path.split('/').length
  //   const fromDepth = from.path.split('/').length
  //   this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
  //   next()
  // },

  watch: {
    $route(to, from) {
      const toDepth = to.path.split("/").length;
      const fromDepth = from.path.split("/").length;
      this.transitionName = toDepth < fromDepth ? "slide-right" : "slide-left";
    }
  }
};
</script>

<style>
/*@import './assets/css/custom.css';*/

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
