<template>
  <Button label="Logout" @click="logout" class="mt-5" />
  <br>
  <br>
  <router-link to="/category">
    <Button label="Category"></Button>
  </router-link>
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import apiClient from '@/helpers/axios'
import Stats from './components/Stats.vue';
import { ref, onMounted } from "vue";
const configure = useAuthStore()

const testToken = async () => {
  try {
    const response = await apiClient.post("login/test-token");
    if (response.error) {
      window.location.assign("/login")
    }
  } catch(err) {
    window.location.assign("/login")
    
  }

}

const logout = async () => {
  configure.logout()
  window.location.assign("/login")
}

onMounted(() => {
  testToken()
})

</script>