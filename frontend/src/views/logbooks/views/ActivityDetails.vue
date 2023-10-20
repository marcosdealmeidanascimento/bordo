<template>
    <router-link :to="{ name: 'postDetails', params: { id: post_id }, query: { logbookId: logbook_id } }">
        <Button icon="pi pi-arrow-left" class="mb-5" />
    </router-link>
</template>

<script setup>
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const router = useRoute();

const post_id = ref(router.query.postId);

</script>