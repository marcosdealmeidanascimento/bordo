<template>
  <div :class="toolbar ? 'header toggle' : 'header'">
    <div class="layout-menu-button">
        <Button icon="pi pi-bars" @click="toggleToolbar"/>
    </div>    
    <div class="layout-topbar-icons">
      <Button type="button" class="px-3 menu-button"  @click="toggleLocation">
        <img alt="logo" :src=image style="width: 2rem" />     
     </Button>
     <Menu ref="menu" :model="items" :popup="true">
      <template #item="{item}">
        <Button v-if="image != item.image" type="button" class="px-3 location-button"  @click="changeLanguage(item)">
          <img alt="logo" style="width: 2rem" :src=item.image />
          <span class="ml-2 font-bold">{{item.label}}</span>     
       </Button>
      </template>
     </Menu>
     <Button type="button" class="px-3 menu-button" @click="logout()">
      <i class="pi pi-power-off pi-fw"></i>
    </Button>
    </div>
  </div>
</template>

<script>
import Menu from 'primevue/menu';
import menuLocale from '../../../helpers/locale/menu.js';
import { useAuthStore, useConfigStore } from '../../../store';
import { mapState, mapActions } from 'pinia'

export default {
  components: { Menu },
  data() {
    return {
      items: menuLocale,
      image: "src/assets/images/flags/us.jpg",    
    }
  },
  computed: {
    // note we are not passing an array, just one store after the other
    // each store will be accessible as its id + 'Store'
    ...mapState(useConfigStore, ['toolbar']),
    
  },
  methods: {
    ...mapActions(useAuthStore, ['login','logout']),
    ...mapActions(useConfigStore, ['setToolbar']),
    toggleToolbar(){
      this.setToolbar()
    },
    toggleLocation(event) {
    this.$refs.menu.toggle(event);
    },    
    changeLanguage(item) {
      this.image = item.image
      this.$i18n.locale  = item.value  
    }, 
  },
};
</script>

<style>
.header {
  position: absolute;
  padding: 0 12px;
  min-height: 50px;
  background: linear-gradient(
    145deg,
    rgb(32, 106, 80) 15%,
    rgb(21, 57, 102) 70%
  );
  top: 0;
  right: 0;
  left: 200px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all .5s ease; 
}
.toggle{
  left: 50px !important;
  transition: all .5s ease;
}
.header .p-button {
  border: 0px !important;
}
.layout-menu-button .p-button{
    color: #fff;
    background-color: transparent !important; 
}
.layout-menu-button .p-button span{
    font-size: 1.5em; 
}
.header .layout-topbar-icons {
  float: right;
  display: block;
  animation-duration: 0.5s;
}
.menu-button{
  color: var(--text-color) !important;
  background-color: transparent !important; 
  border: 0px !important;
}
.location-button{
  color: var(--text-color) !important;
  background-color: transparent !important; 
  border: 0px !important;
  width: 100%;
}
.p-button:hover:enabled{
  color: rgb(18, 40, 206);
  border: 0px !important;
}
.header .pi {
  color: #fff;
  font-size: 1.2rem;
}

</style>
