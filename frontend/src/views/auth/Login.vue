<template>
  <p class="text-5xl flex justify-content-center -my-5">
    Login
  </p>
  <section class="flex justify-content-center">
    <form @submit.prevent="login" class="flex flex-column w-min">

      <label for="username" class="col-fixed">E-mail</label>
      <InputText :autofocus="true" :class="invalid" v-model="user" placeholder="user@example.com" required type="email" />

      <label for="password" class="col-fixed mt-5">Password</label>
      <Password v-model="pw" :class="invalid" :feedback="false" toggleMask required />

      <Button icon="pi pi-send" label="Log In" type="submit" class="mt-5" />
    </form>
  </section>
  <section class="flex flex-column align-items-center -my-6">
    <router-link class="mb-2" style="color: var(--text-color)" to="/register">Don't hava an account? Register
      here</router-link>
    <router-link class="my-2" style="color: var(--text-color)" to="/password-recovery">Forgot your password?</router-link>
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
import { useRouter } from 'vue-router'
import axios from 'axios'

const toast = useToast();
const router = useRouter();
const configure = useAuthStore();

const user = ref("");
const pw = ref("");
const invalid = ref("");
const response = ref();

const show = () => {
  toast.add({ severity: 'error', summary: 'Failed to Log In', detail: 'Incorrect Email or Password', life: 3000 });
};

const login = async () => {
  if (user.value !== "" && pw.value !== "") {

    var data = {
      grant_type: "",
      username: user.value,
      password: pw.value,
      scope: "",
      client_id: "",
      client_secret: "",
    };

    var config = {
      method: "post",
      url: import.meta.env.VITE_SERVER_NAME + "login/access-token",
      headers: {
        accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      data: data,
    };

    console.log(user.value);
    console.log(pw.value);

    try {
      const userData = await axios(config);
      response.value = await configure.login(user.value, pw.value);
      router.push("/");
    } catch(err) {
      invalid.value = "p-invalid";
      show();
    }

  }
}

onMounted(() => {

})

</script>

<style scoped>
section {
  margin: 5rem 2.5rem;
}
</style>