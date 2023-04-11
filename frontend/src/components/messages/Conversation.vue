

<template>
    <div class="conversation">
        <div v-for="message in messages.slice().reverse()" :class="getClass(message) + ' message'">
            <p>{{ message.content }}</p>
        </div>
    </div>
    <input type="text" class="conversation-input" v-model="input" @keypress.enter="onPressEnter">
</template>

<script setup lang="ts">
import { fetcher } from '@/utils/fetcher';
import { ref, defineProps } from 'vue';

const props = defineProps(['contact'])

const input = ref()

const messages = ref([])
fetcher(`http://localhost:5000/messages/${props.contact.id}`)
    .then(response => response.json())
    .then(data => {
        messages.value = data;
    })

function getClass(message: any) {
    if (message.sender_id === props.contact.id) {
        return 'other'
    }
    return 'self'
}

async function onPressEnter() {
    const response = await fetcher(`http://localhost:5000/messages/${props.contact.id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            content: input.value
        })
    })

    if (response.status === 201) {
        const data = await response.json()
        messages.value.push(data)
        input.value = ''
    }
}

</script>

<style scoped>
.conversation {
    display: flex;
    flex-direction: column-reverse;
    gap: 16px;
    padding: 0 16px;

    overflow-y: scroll;
    height: 100%;
}

.message {
    width: 50%;
    padding: 16px;
    border-radius: 8px;
}

.self {
    background-color: #692672;
    color: #fffdfd;
    align-self: flex-end;
}

.other {
    background-color: green;
    color: #fffdfd;
    align-self: flex-start;
}

.conversation-input {
    width: 100%;
    padding: 8px;
    font-size: 18px;
    border: none;
    border-top: 1px solid rgba(0, 0, 0, 0.2);
    background-color: #fffdfd;

    align-self: flex-end;
}

.conversation-input:focus {
    outline: 1px solid #692672;
}
</style>