import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PoemHistory from '../views/PoemHistory.vue'
import PoemGallery from '../views/PoemGallery.vue'
import GeneratePoem from '../views/GeneratePoem.vue'
// Define routes
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // Lazy load the AboutView component
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    // Lazy load the ContactView component
    component: () => import(/* webpackChunkName: "contact" */ '../views/ContactView.vue')
  },
  {
    path: '/history',
    name: 'PoemHistory',
    component: PoemHistory
  },
  {
    path: '/generate',
    name: 'GeneratePoem',
    component: GeneratePoem
  },
  {
    path: '/gallery',
    name: 'PoemGallery',
    component: PoemGallery
  }
]

// Create router instance
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
