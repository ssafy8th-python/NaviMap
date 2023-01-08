import Vue from 'vue'
import VueRouter from 'vue-router'
import ThemeDetailView from '@/views/ThemeDetailView.vue'
import PlaceDetailView from '../views/PlaceDetailView'
import AddPlaceView from '../views/AddPlaceView'
import MainPage from '../views/MainPage'

Vue.use(VueRouter)

const routes = [
  {
    path:"/home",
    name: 'MainPage',
    component: MainPage
  },
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
