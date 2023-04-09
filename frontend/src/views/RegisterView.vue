<template>
    <main>
        <div v-if="error" class="wrapper error">{{ error }}</div>

        <div class="wrapper content">
            <label for="name">Nom</label>
            <input type="name" name="name" v-model="name">
            <label for="email">Email</label>
            <input type="email" name="email" v-model="email">
            <label for="password">Mot de passe</label>
            <input type="password" name="password" v-model="password">
            <label for="password-confirmation">Confirmation mot de passe</label>
            <input type="password" name="password-confirmation" v-model="password_confirmation">
            <div class="actions">
                <button class="primary" @click="register">Soumettre</button>
                <button class="secondary" @click="$router.push('/login')">Se connecter</button>
            </div>
        </div>
    </main>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import 'vue3-carousel/dist/carousel.css'

const router = useRouter()

const name = ref()
const email = ref()
const password = ref()
const password_confirmation = ref()

const error = ref()

async function register() {
    const response = await fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name.value,
            email: email.value,
            password: password.value,
            password_confirmation: password_confirmation.value,
        })
    })

    if (response.status >= 400 && response.status < 500) {
        error.value = 'Email ou mot de passe incorrect'
        return
    }

    if (response.status >= 500) {
        error.value = 'Erreur serveur'
        return
    }

    router.push('/login')
}

</script>
  
<style scoped>
main {
    display: flex;
    justify-content: center;

    margin-top: 36px;
}

.content {
    width: 400px;

    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 16px;
}

.actions {
    padding: 8px;
    display: flex;
    justify-content: space-around;
}

input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 8px;
}

label {
    font-weight: bold;
}
</style>
  