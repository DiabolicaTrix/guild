import { createRouter, createWebHistory } from 'vue-router'
import auth from '../middlewares/auth'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/projects/:id',
      name: 'project',
      component: () => import('../views/projects/ProjectView.vue')
    },
    {
      path: '/users/:id',
      name: 'user',
      component: () => import('../views/users/UserView.vue')
    }
  ]
})

router.beforeEach(auth)

export default router
