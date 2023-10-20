<template>
    <!-- <router-link :to="{ name: 'activityDetails', params: { id: activity_id }, query: { logbookId: logbook_id } }"> -->
    <Card>
        <template #title>
            {{ activity.title }}
        </template>
        <template #content>
            <p v-if="activity.description">
                {{ activity.description }}
            </p>
            <p v-else style="font-style: italic; color: #a0a0a0">
                No description
            </p>
        </template>
    </Card>
    <!-- </router-link> -->
</template>

<script setup>
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";

const activities = defineProps({
    activities: Object,
})

const activity = ref(activities.activities);

</script>