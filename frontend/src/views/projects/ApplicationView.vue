<template>
    <main>
        <div class="project wrapper">
            <header>
                <h1>Application pour {{ application.project.name }}</h1>
            </header>
            <div class="inputs">
                <UserCard :user="application.user" :subtitle="application.role.name"></UserCard>
                <h2>Motivation</h2>
                <p>{{ application.motivation }}</p>
            </div>
            <footer>
                <button v-if="!loading" class="accept" @click="apply">Accepter</button>
                <button v-else class="accept">
                    <sync-loader color="#fffdfd" size="8px"></sync-loader>
                </button>
                <button class="reject" @click="apply">Refuser</button>
            </footer>
        </div>
    </main>
</template>

<script setup lang="ts">
import UserCard from '@/components/UserCard.vue';
import { fetcher } from '@/utils/fetcher';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()

const application = ref()
fetcher(`http://localhost:5000/applications/${route.params.id}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        application.value = data;
    })

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

footer {
    display: flex;
    gap: 16px;
}

.reject {
    background-color: #FF0000;
}

.accept {
    background-color: #148314;
}
</style>