import Vue from 'vue'
import VueRouter from 'vue-router'
import ThemeDetailView from '@/views/ThemeDetailView.vue'
import PlaceDetailView from '../views/PlaceDetailView'
import AddPlaceView from '../views/AddPlaceView'
import LoginView from '../views/LoginView'


Vue.use(VueRouter)

const routes = [
  
  {
    path:"/themedetail",
    name: 'ThemeDetailView',
    component: ThemeDetailView
  },
  {
    path: '/detail',
    name: 'detail',
    component: PlaceDetailView
  },
  {
    path: '/add-place',
    name: 'add-place',
    component: AddPlaceView
  },
  {
    path: '/login',
    name: 'login',
    component :LoginView

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
