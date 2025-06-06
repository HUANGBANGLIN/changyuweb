import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
// 引入全局自定义样式
import './assets/global.css'

router.beforeEach((to, from, next) => {
    const defaultTitle = '昌鈺興業'
    document.title = to.meta.title ? `${to.meta.title} - 昌鈺興業` : defaultTitle
    next()
  })

createApp(App).use(router).mount('#app')
//createApp(App).mount('#app')
