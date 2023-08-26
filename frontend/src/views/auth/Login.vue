<template>
  <section class="flex justify-content-center">

    <form @submit.prevent="login" class="flex flex-column w-min">

      <label for="username" class="col-fixed">E-mail</label>
      <InputText v-model="user" placeholder="user@example.com" required type="email" />

      <label for="password" class="col-fixed mt-5">Password</label>
      <Password v-model="pw" :feedback="false" toggleMask required />

      <Button label="Log In" type="submit" class="mt-5" />
    </form>
  </section>
  <section class="flex flex-column align-items-center -my-6">
    <router-link class="mb-2" style="color: var(--text-color)" to="/register">Don't hava an account? Register here</router-link>
    <router-link class="my-2" style="color: var(--text-color)" to="">Forgot your password?</router-link>
  </section>
  <Toast />
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';

const toast = useToast();

const configure = useAuthStore()

const user = ref("");
const pw = ref("");
const invalid = ref("");
const response = ref();

const show = () => {
    toast.add({ severity: 'error', summary: 'Failed to Log In', detail: 'Incorrect Email or Password', life: 3000 });
};

const login = async () => {
  if (user.value !== "" && pw.value !== "") {

    response.value = await configure.login(user.value, pw.value);
    if (response.value == 0) {
      show()
    } else {
      location.assign("/")
    }

  }
}

onMounted(() => {

})

</script>