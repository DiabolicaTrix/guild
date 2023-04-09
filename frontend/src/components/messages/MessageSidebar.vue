

<template>
    <div class="contacts">
        <div class="contacts-header">
            <h2 v-if="activeContact">
                <font-awesome-icon class="icon clickable" :icon="['fas', 'caret-left']" @click="activeContact = null" />
                {{ activeContact.name }}
            </h2>
            <h2 v-else>Contacts</h2>
        </div>
        <Contacts v-if="!activeContact" @select="select"></Contacts>
        <Conversation v-else :contact="activeContact"></Conversation>
    </div>
</template>

<script setup lang="ts">
import Contacts from '@/components/messages/Contacts.vue';
import Conversation from '@/components/messages/Conversation.vue';
import { fetcher } from '@/utils/fetcher';

import { ref } from 'vue';

const activeContact = ref()
function select(contact: any) {
    activeContact.value = contact
}
</script>

<style scoped>
.contacts {
    border-top-right-radius: 8px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    background-color: #fffdfd;

    display: flex;
    flex-direction: column;
    gap: 16px;
}

.contacts-header {
    padding: 16px;
    background-color: #692672;
    color: #fffdfd
}
</style>