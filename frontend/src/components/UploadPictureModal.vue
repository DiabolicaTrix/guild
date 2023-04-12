<template>
    <div class="container" @keydown.esc="close">
        <div class="wrapper modal">
            <header>
                <h1>Ajouter une image</h1>
            </header>
            <input type="file" name="filename" ref="file">
            <footer>
                <button class="primary" @click="add">Soumettre</button>
                <button class="cancel-button" @click="close">Annuler</button>
            </footer>
        </div>
    </div>
</template>

<script setup lang="ts">
import { fetcher } from '@/utils/fetcher';
import { ref } from 'vue';

const props = defineProps(['userId'])
const emit = defineEmits(['add'])

const file = ref()

async function add() {
    if (!file) {
        close()
    }

    const data = new FormData()
    data.append('file', file.value.files[0])

    await fetcher(`http://localhost:5000/users/${props.userId}/picture`, {
        method: 'POST',
        headers: {
            'Content-Type': 'multipart/form-data'
        },
        body: data
    })
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

.error {
    color: red;
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