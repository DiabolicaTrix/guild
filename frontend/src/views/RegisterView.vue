<template>
    <main>
        <div v-if="errors.request" class="wrapper error">{{ errors.request }}</div>

        <div class="wrapper content">
            <label for="name">Nom</label>
            <input type="name" name="name" v-model="name">
            <span v-if="errors.name" class="inline-error">{{ errors.name }}</span>
            <label for="email">Email</label>
            <input type="email" name="email" v-model="email">
            <span v-if="errors.email" class="inline-error">{{ errors.email }}</span>
            <label for="password">Mot de passe</label>
            <input type="password" name="password" v-model="password">
            <span v-if="errors.password" class="inline-error">{{ errors.password }}</span>
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
import { validateName, validateEmail, validatePassword } from '@/validations/registervalidation';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import 'vue3-carousel/dist/carousel.css'

const router = useRouter()

const name = ref()
const email = ref()
const password = ref()
const password_confirmation = ref()

type RegisterErrors = {
    request?: string
    name?: string
    email?: string
    password?: string
}
const errors = ref<RegisterErrors>({})

async function register() {
    const nameValidation = validateName(name.value)
    errors.value.name = nameValidation
    const emailValidation = validateEmail(email.value)
    errors.value.email = emailValidation
    const passwordValidation = validatePassword(password.value, password_confirmation.value)
    errors.value.password = passwordValidation

    // If any of the validations failed, return
    if (nameValidation || emailValidation || passwordValidation) {
        return
    }

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
        errors.value.request = 'Email ou mot de passe incorrect'
        return
    }

    if (response.status >= 500) {
        errors.value.request = 'Erreur serveur'
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
  