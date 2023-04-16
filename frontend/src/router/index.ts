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
          path: '/discover',
          name: 'discover',
          component: () => import('../views/DiscoverView.vue')
        },
        {
          path: '/me',
          name: 'me',
          component: () => import('../views/users/SelfView.vue')
        },
        {
          path: '/applications/:id',
          name: 'application',
          component: () => import('../views/projects/ApplicationView.vue')
        },
        {
          path: '/projects/create',
          name: 'project-create',
          component: () => import('../views/projects/ProjectCreateView.vue')
        },
        {
          path: '/projects/:id',
          name: 'project',
          component: () => import('../views/projects/ProjectView.vue')
        },
        {
          path: '/projects/:projectId/apply/:roleId',
          name: 'project-apply',
          component: () => import('../views/projects/ApplyView.vue')
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
