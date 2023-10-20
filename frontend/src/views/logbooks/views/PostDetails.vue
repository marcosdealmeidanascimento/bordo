<template>
    <router-link :to="{ name: 'logbookDetails', params: {id: logbook_id} }">
        <Button icon="pi pi-arrow-left" class="mb-5" />
    </router-link>
    <Button @click="visible = true" label="Create Activity" class="mt-5" />
    <Dialog v-model:visible="visible" modal maximizable header="Create Activity">
        <form @submit.prevent="createActivity">
            <div class="flex flex-column">
                <InputText class="mb-5" v-model="title" placeholder="Title" required autofocus />
                <InputText class="mb-5" v-model="description" placeholder="Description" />
                <Dropdown class="mb-5" placeholder="Select a Category" :options="categories" optionLabel="name"
                v-model="selectedCategory" filter />
                <Calendar class="mb-5" placeholder="Started at" v-model="init_time" timeOnly />
                <Calendar class="mb-5" placeholder="Ended at" v-model="end_time" timeOnly />
                <Button label="Create Activity" type="submit" class="mt-5" />
            </div>
        </form>
    </Dialog>
    <div class="grid">
        <div class="col-6 p-3" v-for="activity in activities">
            <Activity :activities="activity" />
        </div>
    </div>
    <Toast />
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import apiClient from '@/helpers/axios'
import Toast from "primevue/toast";
import { useToast } from "primevue/usetoast";
import Calendar from "primevue/calendar";
import Dropdown from "primevue/dropdown";
import Activity from "../components/Activity.vue";

const route = useRoute();
const toast = useToast();

const visible = ref(false);
const user_id = ref();

const title = ref();
const description = ref();
const init_time = ref();
const end_time = ref();
const category_id = ref();
const selectedCategory = ref();
const post_id = ref(route.params.id)
const categories = ref();
const activities = ref([]);
const logbook_id = ref(route.query.logbookId);

const getActivities = async () => {
    const response = await apiClient.get("activity/post/" + post_id.value);
    activities.value = response.data;
}

const createActivity = async () => {
    visible.value = false;
    category_id.value = selectedCategory.value != undefined ? selectedCategory.value.id : null;
    end_time.value = new Date(end_time.value).getHours() + ":" + new Date(end_time.value).getMinutes();
    
    try {
        const response = await apiClient.post("activity", {
            title: title.value,
            description: description.value,
            init_time: init_time.value,
            end_time: end_time.value,
            category_id: category_id.value,
            user_id: user_id.value,
            post_id: post_id.value,
        });
        if (response.error) {
            toast.add({
                severity: "error",
                summary: "Error",
                detail: "Activity not created",
            });
        } else {
            toast.add({
                severity: "success",
                summary: "Success",
                detail: "Activity created successfully",
            });

        }
        getActivities();
    } catch (error) {
        toast.add({
            severity: "error",
            summary: "Error",
            detail: "Activity not created",
        });
    }

}

const getCategories = async () => {
    const response = await apiClient.get("category");
    categories.value = response.data;
}

onMounted(() => {
    const user = JSON.parse(localStorage.getItem("user"))
    user_id.value = user.id
    init_time.value = new Date().getHours() + ":" + new Date().getMinutes();
    getCategories();
    getActivities();
})

</script>