import { createRouter, createWebHistory } from 'vue-router'
import BaseLayout from '@/layout/BaseLayout.vue'
const routes = [
  {
    path: '/',
    component: BaseLayout,
    redirect: 'dashboard',
    meta: {
      authRequired: true,
      hidden: true,
    },
    children: [
      { 
        path: '/dashboard',
        name: 'dashboard', 
        component: () => import('@/views/home/Dashboard.vue'),
        meta: { transition: 'slide-right' },
       },
      { 
        path: '/permission',
        name: 'permission', 
        component: () => import('@/views/user/permissions/index.vue'),
        meta: { transition: 'slide-right' },
       },
       { 
         path: '/roles',
         name: 'roles', 
        component: () => import('../views/user/roles/index.vue'),
         meta: { transition: 'slide-right' },
        }
    ],
  },
  { 
    path: '/login',
    name: 'dashboard', 
    component: () => import('../views/auth/Login23.vue'),
    meta: { transition: 'slide-right' },
   },  

]

const router = createRouter({
        history: createWebHistory(),
        routes
      })
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record)) {
    next()
  } else {
    console.log('Not auth required')
    next()
  }
});

export default router