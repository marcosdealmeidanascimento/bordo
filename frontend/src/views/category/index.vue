<template>
    <div>
        <h1>Category</h1>
    </div>
    <div>
        <router-link to="/home">Voltar</router-link>
    </div>
    <form @submit.prevent="createCategory">
        <div class="flex">
            <div class="mr-5">
                <p>Name</p>
                <InputText v-model="name" required placeholder="Name" />
            </div>
            <div>
                <p>Description</p>
                <Textarea v-model="description" rows="5" cols="30" placeholder="Description" />
            </div>
        </div>
        <Button type="submit" label="Create Category" />
    </form>

    <Dropdown placeholder="Select a Category" :options="categories" optionLabel="name" v-model="selectedCategory" filter />

    <Toast />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/helpers/axios';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import Dropdown from 'primevue/dropdown';

const toast = useToast();
const name = ref("");
const description = ref("");
const categories = ref([]);
const selectedCategory = ref("");

const createCategory = async () => {
    try {
        const response = await apiClient.post("category", {
            name: name.value,
            description: description.value
        });
        if (response.error) {
            toast.add({ severity: 'error', summary: 'Failed to Create a Category', detail: 'An error ocurred while creating this category', life: 3000 });
        }else{
            toast.add({ severity: 'success', summary: 'Category Created', detail: 'Category Created with Success', life: 3000 });
            setTimeout(() => {
                name.value = "";
                description.value = "";
            }, 3000);
        }
    } catch(err) {
        toast.add({ severity: 'error', summary: 'Failed to Create a Category', detail: 'An error ocurred while creating this category', life: 3000 });
    }
}

const getCategories = async () => {
    try {
        const response = await apiClient.get("category");
        categories.value = response.data;
    } catch {
        toast.add({ severity: 'error', summary: 'Failed to Get Categories', detail: 'An error ocurred while getting categories', life: 3000 });
    }
}

onMounted(() => {

    getCategories();

})

</script>