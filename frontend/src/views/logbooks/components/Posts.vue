<template>
    <router-link :to="{ name: 'postDetails', params: { id: post_id }, query: { logbookId: logbook_id } }">
        <Card>
            <template #title>
                {{ post.title }}
            </template>
            <template #content>
                <p v-if="post.description">
                    {{ post.description }}
                </p>
                <p v-else style="font-style: italic; color: #a0a0a0">
                    No description
                </p>
            </template>
        </Card>
    </router-link>
</template>

<script setup>
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";

const posts = defineProps({
    posts: Object,
})

const post = ref(posts.posts);
const post_id = ref(post.value.id);
const logbook_id = ref(post.value.logbook_id);

</script>