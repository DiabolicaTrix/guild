

<template>
    <div v-if="loading" class="loader">
        <sync-loader v-if="loading" color="grey" size="16px"></sync-loader>
    </div>
    <div v-else v-for="contact in contacts" class="contact">
        <UserCard :user="contact" navigate="no" @click="$emit('select', contact)"></UserCard>
    </div>
</template>

<script setup lang="ts">
import UserCard from '@/components/UserCard.vue';
import { fetcher } from '@/utils/fetcher';

import { ref } from 'vue';

const emits = defineEmits(['select'])

const loading = ref(true)
const contacts = ref([])
fetcher(`http://localhost:5000/messages`)
    .then(response => response.json())
    .then(data => {
        contacts.value = data;
        loading.value = false;
    })

</script>

<style scoped>
.contact {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 0 16px;
    cursor: pointer;
}

.loader {
    display: flex;
    justify-content: center;
}
</style>