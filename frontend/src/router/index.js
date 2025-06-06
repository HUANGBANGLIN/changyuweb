// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import first from '../views/first.vue'
import HelloWorld from '../components/HelloWorld.vue'
import index from '../views/index.vue'
import about from '../views/about.vue'
import service from '../views/service.vue'
import projectshare from '../views/projectshare.vue'
import contact from '../views/contact.vue'
import socialresponsibility from '../views/socialresponsibility.vue'

const routes = [
  { path: '/', component: HelloWorld, meta: { title: '首頁' }},
  { path: '/first', component: first, meta: { title: '首頁' } },
  { path: '/index', component: index, meta: { title: '首頁' }},
  { path: '/about', component: about, meta: { title: '關於我們' }},
  { path: '/service', component: service, meta: { title: '服務項目' }},
  { path: '/projectshare', component: projectshare, meta: { title: '業務實績' }},
  { path: '/contact', component: contact, meta: { title: '聯絡我們' }},
  { path: '/socialresponsibility', component: socialresponsibility, meta: { title: '企業社會責任' }}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
