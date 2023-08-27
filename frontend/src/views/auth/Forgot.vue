<template>
    <section class="flex justify-content-center">

        <form @submit.prevent="reset" class="flex flex-column w-min">

            <label for="username" class="col-fixed">E-mail</label>
            <InputText :autofocus="true" :class="invalid" v-model="user" placeholder="user@example.com" required
                type="email" />

            <Button label="Send Request" type="submit" class="mt-5" />
        </form>
    </section>
    <section class="flex flex-column align-items-center -my-6">
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
import { useRouter } from 'vue-router'

const toast = useToast();
const router = useRouter();
const configure = useAuthStore();

const user = ref("");
const pw = ref("");
const invalid = ref("");
const response = ref();

const show = () => {
    toast.add({ severity: 'error', summary: 'Failed to Read E-mail address', detail: 'Fill out the field with your E-mail address', life: 3000 });
};

const reset = async () => {

    const data = {
        email: user.value
    }
    console.log(data);

    const response = await apiClient.post("/password-recovery", data)

    // router.push("/");


}

onMounted(() => {

})

</script>
  
<style scoped>
section {
    margin: 5rem 2.5rem;
}
</style>