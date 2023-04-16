<template>
    <main>
        <div class="wrapper content">
            <div v-if="errors.request" class="wrapper error">{{ errors.request }}</div>
            <label for="email">Email</label>
            <input type="email" name="email" v-model="email">
            <span v-if="errors.email" class="inline-error">{{ errors.email }}</span>
            <label for="password">Mot de passe</label>
            <input type="password" name="password" v-model="password">
            <span v-if="errors.password" class="inline-error">{{ errors.password }}</span>
            <div class="actions">
                <button class="primary" @click="login">Se connecter</button>
                <button class="secondary" @click="register">S'inscrire</button>
            </div>
        </div>
    </main>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCookies } from "vue3-cookies";

import 'vue3-carousel/dist/carousel.css'
import { useSessionStore } from '@/stores/session.js';
import { extractUserFromSession } from '@/utils/session';
import { validateEmail, validatePassword } from '@/validations/loginvalidation';

const router = useRouter()
const { cookies } = useCookies()
const { setSession } = useSessionStore()

const email = ref()
const password = ref()

type LoginErrors = {
    request?: string
    email?: string
    password?: string
}
const errors = ref<LoginErrors>({})

async function login() {
    const emailValidation = validateEmail(email.value)
    errors.value.email = emailValidation
    const passwordValidation = validatePassword(password.value)
    errors.value.password = passwordValidation

    if (emailValidation || passwordValidation) {
        return
    }

    const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email.value,
            password: password.value
        })
    })

    if (response.status >= 400 && response.status < 500) {
        errors.value.request = 'Email ou mot de passe incorrect'
        return
    }

    if (response.status >= 500) {
        errors.value.request = 'Erreur serveur'
        return
    }

    let data = await response.json()
    cookies.set('token', data.token)
    setSession(extractUserFromSession())
    await router.push('/')
    router.go(0)
}

function register() {
    router.push('/register')
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
  