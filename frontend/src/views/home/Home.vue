<template>
    <Stats />
    <button @click="teste">Take</button>
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import apiClient from '@/helpers/axios'
import Stats from './components/Stats.vue';
import { ref, onMounted } from "vue";
const configure = useAuthStore()

const teste = async() => {
  configure.login("teste@teste.com","string")
  const response = await apiClient.get("users"); 
  console.log(response.data)
}

onMounted(() => {
    configure.checkLoginState()
})

</script>