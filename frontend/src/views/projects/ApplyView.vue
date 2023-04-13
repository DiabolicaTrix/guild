<template>
    <main>
        <div class="project wrapper">
            <header>
                <h1>Appliquer pour le projet</h1>
            </header>
            <div class="inputs">
                <h2>Projet: {{ project.name }}</h2>
                <h2>Rôle: {{ role.name }}</h2>
                <label for="motivation">Motivation</label>
                <textarea name="motivation" v-model="motivation"></textarea>
            </div>
            <footer>
                <button v-if="!loading" class="primary" @click="apply">Appliquer</button>
                <button v-else class="primary">
                    <sync-loader color="#fffdfd" size="8px"></sync-loader>
                </button>
            </footer>
        </div>
    </main>
</template>

<script setup lang="ts">
import { fetcher } from '@/utils/fetcher';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()

const project = ref()
fetcher(`http://localhost:5000/projects/${route.params.projectId}`)
    .then(response => response.json())
    .then(data => {
        project.value = data;
    })

const role = ref()
fetcher(`http://localhost:5000/roles/${route.params.roleId}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        role.value = data;
    })

const motivation = ref()

const loading = ref(false)
async function apply() {
    loading.value = true
    const response = await fetcher(`http://localhost:5000/roles/${route.params.roleId}/apply`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            motivation: motivation.value
        })
    })
    loading.value = false
}


</script>

<style scoped>
main {
    display: flex;
    justify-content: center;
    margin-top: 36px;
}

.project {
    width: 500px;
    padding: 16px;

    display: flex;
    flex-direction: column;
    gap: 16px;
}

.inputs {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.inputs textarea input {
    font-size: 18px !important;
}
</style>