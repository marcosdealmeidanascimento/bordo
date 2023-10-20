<template>
    <router-link to="/logbooks">
        <Button icon="pi pi-arrow-left" class="mb-5" />
    </router-link>

    <Button @click="visible = true" label="Create Post" class="mt-5" />
    <Dialog v-model:visible="visible" modal maximizable header="Create Post">
        <form @submit.prevent="createPost">
            <div class="flex flex-column">
                <InputText class="mb-5" v-model="title" placeholder="Title" required autofocus />
                <InputText class="mb-5" v-model="description" placeholder="Description" />
                <Calendar class="mb-5" v-model="date" placeholder="Date" dateFormat="mm/dd/yy" />
                <Button label="Create Post" type="submit" class="mt-5" />
            </div>
        </form>
    </Dialog>
    <Toast />
    <div class="grid">
        <div class="col-6 p-3" v-for="post in posts">
            <Posts :posts="post" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import apiClient from '@/helpers/axios'
import Toast from "primevue/toast";
import { useToast } from "primevue/usetoast";
import Calendar from 'primevue/calendar';
import Posts from "../components/Posts.vue";

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

const getPostsByLogbookAndUser = async () => {
    const data = {
        logbook_id: logbook_id.value,
        user_id: user_id.value
    }
    const response = await apiClient.post("post/logbook/user/", data);
    posts.value = response.data;
}

const getLogbook = async () => {
    const response = await apiClient.get("logbook/" + logbook_id.value);
    logbook.value = response.data;
}

const createPost = async () => {
    visible.value = false;
    date.value = new Date(date.value).toLocaleDateString();

    const dateArray = date.value.split("/");
    date.value = dateArray[2] + "-" + dateArray[0] + "-" + dateArray[1];

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
    date.value = new Date().toLocaleDateString();
    getPostsByLogbookAndUser();
}

onMounted(() => {
    date.value = new Date().toLocaleDateString();
    logbook_id.value = route.params.id;
    const user = JSON.parse(localStorage.getItem("user"))
    user_id.value = user.id

    getLogbook();
    getPostsByLogbookAndUser();
})

</script>