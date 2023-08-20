<template>
  <aside  :class="toolbar ? 'toggle_aside' : ''">
    
    <nav>
      <div>
        <div class="py-2 px-2 m-0">
            <a href="#" class="logo"><img src="https://www.primefaces.org/atlantis-vue/layout/images/logo-light.png" style="height: 30px"/>
              <div class="logo_name"></div>
            </a>
        </div>
        <hr class="mb-5">
      <Menu></Menu>
    </div>
    </nav>
  </aside>
</template>

<script setup>
import Menu from './menu/index.vue';
import {getMenuData} from '@/helpers/menu'
import { useConfigStore } from '@/store';
import { storeToRefs } from 'pinia';
const store = useConfigStore()
const { toolbar } = storeToRefs(store);
const list = getMenuData

</script>

<style>
aside {
  transform: translateX(0px);
  background-image: url(https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg) !important;
  background-size: cover !important;
  position: fixed;
  top: 0;
  bottom: 0;
  background: #fff;
  z-index: 1000;
  width: 200px;
  transition: all .5s ease;
  color: var(--text-color);
}
.link{
  margin-left: 10px;
}
.logo_name {
  font-size: 25px;
  font-weight: 600;
  transition: all .5s ease;
  display: block;
  color: var(--green-600);
  }
  .logo{
    display: flex !important;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 10px;
    text-decoration: none;
  }
.toggle_aside{
  width: 50px !important;
  transition: all .5s ease;
}
.toggle_aside .logo_name {  
  display: none;
}
.toggle_aside .link{
  margin-left: 10px;
  display: block;
  position: absolute;
  background: rgba(255,255,255,0.5);
  border-radius: 100%;
  transform: scale(0);
  pointer-events: none;
}

nav {
  height: 100%;
  width: 100%;
  background-color: rgba(1, 1, 1, 0.75);
  color: var(--text-color) !important;
}
</style>
