import Vue from "vue";
import Router from "vue-router";
import HelloAcai from "../components/HelloAcai";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "HelloAcai",
      component: HelloAcai
    }
  ]
});
