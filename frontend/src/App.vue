<template>
  <div class="d-flex flex-column min-vh-100">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-md navbar-dark bg-primary px-3">
      <router-link class="navbar-brand" to="/">LOGO 昌鈺興業</router-link>

      <!-- 漢堡按鈕 -->
      <button
        class="navbar-toggler"
        type="button"
        @click="isOpen = !isOpen"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- 導覽連結區 -->
      <div class="collapse navbar-collapse" :class="{ show: isOpen }" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item" v-for="item in navItems" :key="item.to">
            <router-link
              class="nav-link"
              :to="item.to"
              @click="isOpen = false"
            >{{ item.label }}</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- 主內容 -->
    <div class="flex-fill">
      <router-view />
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3 mt-auto">
      <div>© 2025 昌鈺興業股份有限公司. All rights reserved.</div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isOpen = ref(false)
const navItems = [
  { to: '/', label: '首頁' },
  { to: '/about', label: '關於我們' },
  { to: '/service', label: '服務項目' },
  { to: '/projectshare', label: '業務實績' },
  { to: '/socialresponsibility', label: '企業社會責任' },
  { to: '/contact', label: '聯絡我們' }
]
</script>

<style scoped>
.navbar-nav .nav-link,
.navbar-brand {
  font-weight: 500;
  font-size: 1.1rem;
}

@media (min-width: 768px) {
  .navbar-nav .nav-link,
  .navbar-brand {
    font-size: 1.25rem;
  }
}

@media (min-width: 992px) {
  .navbar-nav .nav-link,
  .navbar-brand {
    font-size: 1.35rem;
  }
}
</style>
