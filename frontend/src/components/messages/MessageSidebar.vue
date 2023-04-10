

<template>
    <div class="contacts" v-if="!collapsed">
        <div class="contacts-header">
            <h2 v-if="activeContact">
                <font-awesome-icon class="icon clickable" :icon="['fas', 'caret-left']" @click="activeContact = null" />
                {{ activeContact.name }}
            </h2>
            <h2 v-else>Contacts</h2>
            <font-awesome-icon class="icon clickable" :icon="['fas', 'minus']" @click="collapsed = true" />
        </div>
        <Contacts v-if="!activeContact" @select="select"></Contacts>
        <Conversation v-else :contact="activeContact"></Conversation>
    </div>
    <div class="contacts collapsed" v-else>
        <div class="contacts-header">
            <h2>Contacts</h2>
            <font-awesome-icon class="icon clickable" :icon="['fas', 'plus']" @click="collapsed = false" />
        </div>
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

const collapsed = ref(true)
</script>

<style scoped>
.contacts {
    border-top-right-radius: 8px;
    border: 1px solid rgba(0, 0, 0, 0.2);
    background-color: #fffdfd;

    display: flex;
    flex-direction: column;
    gap: 16px;

    z-index: 10;
}

.contacts-header {
    border-top-right-radius: 8px;

    padding: 16px;
    background-color: #692672;
    color: #fffdfd;

    display: flex;
    align-items: center;
    justify-content: space-between;
}

.contacts.collapsed {
    top: unset;
    bottom: 0;
}
</style>