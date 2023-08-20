<script setup>
import  Navbar from '../layout/components/app-navbar/Navbar.vue'
import  Sidebar from '../layout/components/sidebar/Sidebar.vue'
import { useConfigStore } from '@/store';
import { storeToRefs } from 'pinia';
const store = useConfigStore()
const { toolbar } = storeToRefs(store);
</script>

<template>
    <section :class="toolbar ? 'section-toggle' : ''"> 
        <router-view />
    </section>
    <Navbar></Navbar>
    <Sidebar></Sidebar>    
</template>

<style>
body {
  margin: 0 !important;
  background-color: var(--surface-ground);
}
section{
    margin-top: 100px;
    margin-right:30px ;
    margin-left:250px ;
    }
.section-toggle{
    margin-left: 100px;
}    
</style>