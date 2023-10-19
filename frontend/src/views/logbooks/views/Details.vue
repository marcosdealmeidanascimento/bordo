<template>
    <router-link to="/logbooks">Voltar</router-link>
    <Button @click="visible = true" label="Create Post" class="mt-5" />
    <Dialog v-model:visible="visible" modal maximizable header="Create Post">
        <form @submit.prevent="createPost">
            <div class="flex flex-column">
                <InputText class="mb-5" v-model="title" placeholder="Title" required autofocus />
                <InputText class="mb-5" v-model="description" placeholder="Description" />
                <Calendar class="mb-5" v-model="date" placeholder="Date" dateFormat="yy-mm-dd" />
                <Button label="Create Post" type="submit" class="mt-5" />
            </div>
        </form>
    </Dialog>
    <Toast />
    {{ posts }}
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import apiClient from '@/helpers/axios'
import Toast from "primevue/toast";
import { useToast } from "primevue/usetoast";
import Calendar from 'primevue/calendar';


const route = useRoute();
const toast = useToast();

const visible = ref(false);
const posts = ref([]);
const logbook_id = ref(route.params.id);
const user_id = ref();
const logbook = ref();

const title = ref();
const description = ref();
const date = ref();

const getPosts = async () => {
    const response = await apiClient.get("post/logbook/" + logbook_id.value);
    posts.value = response.data;
}

const getLogbook = async () => {
    const response = await apiClient.get("logbook/" + logbook_id.value);
    logbook.value = response.data;
    user_id.value = logbook.value.user_id;
}

const createPost = async () => {
    date.value = new Date(date.value).toLocaleDateString();

    const dateArray = date.value.split("/");
    date.value = dateArray[2] + "-" + dateArray[0] + "-" + dateArray[1];

    console.log(date.value);
    try {
        const response = await apiClient.post("post", {
            title: title.value,
            description: description.value,
            date: date.value,
            user_id: user_id.value,
            logbook_id: logbook_id.value
        });
        if (response.error) {
            toast.add({
                severity: 'error',
                summary: 'Error',
                detail: 'Post not created',
                life: 3000
            });
            title.value = "";
            description.value = "";
            date.value = "";
        } else {
            toast.add({
                severity: 'success',
                summary: 'Success',
                detail: 'Post created',
                life: 3000
            });
            visible.value = false;
        }
    } catch {
        toast.add({
            severity: 'error',
            summary: 'Error',
            detail: 'Post not created',
            life: 3000
        });
    }
    title.value = "";
    description.value = "";
    date.value = "";
    getPosts();
}

onMounted(() => {
    logbook_id.value = route.params.id;
    getLogbook();
    getPosts();
})

</script>