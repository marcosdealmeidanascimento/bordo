<template>
    <router-link :to="{ name: 'logbookDetails', params: {id: logbook_id} }">

        <Card>
            <template #title>
                {{ logbook.name }}
            </template>
            <template #content>
                <p v-if="logbook.description">
                    {{ logbook.description }}
                </p>
                <p v-else style="font-style: italic; color: #a0a0a0">
                    No description
                </p>
            </template>
        </Card>
    </router-link>
    <Dialog v-model:visible="visible" modal :header="logbook.name" maximizable>
        <form @submit.prevent="createPost">
            <div class="flex flex-column">
                <InputText class="mb-5" placeholder="Title" required />
                <InputText class="mb-5" placeholder="Description" />
                <Calendar class="mb-5" placeholder="Date" />
                <Button label="Create Post" type="submit" class="mt-5" />
            </div>
        </form>
        <Toast />
        {{ posts }}
    </Dialog>
</template>

<script setup>
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";
import Calendar from 'primevue/calendar';
import Toast from "primevue/toast";
import { useToast } from "primevue/usetoast";

const toast = useToast();

const logbooks = defineProps({
    logbook: Object,
})
const logbook = ref(logbooks.logbook);
const visible = ref(false);

const title = ref("");
const description = ref("");
const date = ref();
const user_id = ref(logbook.value.user_id);
const logbook_id = ref(logbook.value.id);

const posts = ref([]);

const createPost = async () => {
    try {
        const response = await apiClient.post("post", {
            title: title.value,
            description: description.value,
            date: date.value,
            user_id: user_id.value,
            logbook_id: logbook_id.value,
        });
        toast.add({
            severity: 'success',
            summary: 'Post created with success!',
            life: 3000
        });
        posts.value = [...posts.value, response.data];
        getPosts();
    } catch {
        toast.add({
            severity: 'error',
            summary: 'Failed to create post',
            detail: 'Please try again later',
            life: 3000
        });
    }
}

const getPosts = async () => {
    const response = await apiClient.get("post/logbook/" + logbook_id.value);
    posts.value = response.data;

}

const openModal = async () => {
    visible.value = true;
    getPosts();
}


</script>