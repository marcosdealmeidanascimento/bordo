<template>
  <section class="flex justify-content-center">

    <form @submit.prevent="register" class="flex flex-column w-min">

      <label for="fullname" class="col-fixed mt-5">Full Name</label>
      <InputText v-model="fullname" placeholder="Full Name" required />

      <label for="username" class="col-fixed mt-2">E-mail</label>
      <InputText v-model="user" placeholder="user@example.com" required type="email" />

      <label for="password" class="col-fixed mt-5">Password</label>
      <Password v-model="pw" toggleMask required :class="invalidPw"/>

      <label for="password" class="col-fixed mt-2">Confirm Password</label>
      <Password v-model="confpw" :feedback="false" toggleMask required :class="invalidPw" />

      <Button label="Register" type="submit" class="mt-5" />
    </form>
  </section>
  <section class="flex justify-content-center -my-6">
    <router-link class="p-primary" to="/login">Already have an account? Login here.</router-link>
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
const fullname = ref("");
const pw = ref("");
const confpw = ref("");
const invalidPw = ref("");
const invalidEmail = ref("");
const users = ref();

const show = () => {
  toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Incorrect Email or Password', life: 3000 });
};


const register = async () => {
  if (pw.value.length < 6 || pw.value.length > 12) {
    toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Password length must be greater than 6 and less than 12', life: 3000 });
    invalidPw.value = "p-invalid"

  } else if (pw.value !== confpw.value) {
    toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Passwords must be equal', life: 3000 });
    invalidPw.value = "p-invalid"
  } else {
    invalidPw.value = ""
  }

  if (!user.value.includes('.com')) {
    toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Not a valid E-mail', life: 3000 });
    invalidEmail.value = "p-invalid"
  }

  const data = {
    fullname: fullname.value,
    password: confpw.value,
    email: user.value,
  }

}

onMounted(() => {

})

</script>