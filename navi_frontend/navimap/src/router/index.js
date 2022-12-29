import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ThemeDetailView from '@/views/ThemeDetailView.vue'

Vue.use(VueRouter)

const routes = [
  
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:"/themedetail",
    name: 'ThemeDetailView',
    component: ThemeDetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
