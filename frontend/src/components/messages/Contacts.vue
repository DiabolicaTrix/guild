

<template>
    <div v-for="contact in contacts" class="contact">
        <UserCard :user="contact" navigate="no" @click="$emit('select', contact)"></UserCard>
    </div>
</template>

<script setup lang="ts">
import UserCard from '@/components/UserCard.vue';
import { fetcher } from '@/utils/fetcher';

import { ref } from 'vue';

const emits = defineEmits(['select'])

const contacts = ref([])
fetcher(`http://localhost:5000/messages`)
    .then(response => response.json())
    .then(data => {
        contacts.value = data;
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
</style>