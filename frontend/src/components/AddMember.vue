<template>
    <div class="container" @keydown.esc="close">
        <div class="wrapper modal">
            <header>
                <h1>Ajouter un membre</h1>
            </header>
            <label for="email">Email de l'utilisateur</label>
            <input type="text" name="email" v-model="email" />
            <p class="error" v-if="error">Cet utilisateur n'existe pas.</p>
            <label for="role">Rôle de l'utilisateur</label>
            <input type="text" name="role" v-model="role" />
            <footer>
                <button class="primary" @click="add">Ajouter</button>
                <button class="cancel-button" @click="close">Annuler</button>
            </footer>
        </div>
    </div>
</template>

<script setup lang="ts">
import { fetcher } from '@/utils/fetcher';
import { ref } from 'vue';

const emit = defineEmits(['add'])

const email = ref()
const role = ref()
const error = ref(false)

async function add() {
    const response = await fetcher(`http://localhost:5000/users?email=${email.value}`)

    if (response.status == 404) {
        error.value = true
    } else {
        const data = await response.json()
        emit('add', {
            user: data,
            role: role.value
        })
    }
}

function close() {
    emit('add')
}
</script>

<style>
.modal {
    width: 500px;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    padding: 16px;

    display: flex;
    flex-direction: column;
    gap: 8px;
}

.container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-color: rgba(0, 0, 0, 0.7);

    z-index: 10;
}

.cancel-button {
    background-color: #ccc;
    color: #000;
}

footer {
    display: flex;
    gap: 8px;
}
</style>