import { createRouter, createWebHistory } from 'vue-router'
import auth from '../middlewares/auth'
import AppWrapper from '../AppWrapper.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
      path: '/',
      name: 'root',
      component: AppWrapper,
      children: [
        {
          path: '/',
          name: 'home',
          component: () => import('../views/HomeView.vue')
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
    },
  ]
})

router.beforeEach(auth)

export default router
