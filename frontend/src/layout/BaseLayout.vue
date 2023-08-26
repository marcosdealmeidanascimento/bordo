<template>
    <section>
        <router-view />
    </section>
</template>

<script setup>
import { useConfigStore } from '@/store';
import { storeToRefs } from 'pinia';
const store = useConfigStore()
const { toolbar } = storeToRefs(store);
</script>


<style>
body {
    margin: 0 !important;
    background-color: var(--surface-ground);
}

section {
    margin: 5rem 2.5rem;
}
</style>