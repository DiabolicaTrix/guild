<template>
    <main>
        <AddMember v-if="adding" @add="add" />
        <div class="project wrapper">
            <header>
                <h1>Créer un projet</h1>
            </header>
            <div class="inputs">
                <div v-if="errors.request" class="wrapper error">{{ errors.request }}</div>

                <label for="name">Nom du projet</label>
                <input type="text" name="name" v-model="name" />
                <span v-if="errors.name" class="inline-error">{{ errors.name }}</span>
                <label for="description">Description du projet</label>
                <textarea name="description" v-model="description"></textarea>
                <span v-if="errors.description" class="inline-error">{{ errors.description }}</span>
                <div class="members">
                    <label for="members">Membres</label>
                    <UserCard class="member" v-for="member in members" navigate="no" :user="member.user"
                        :subtitle="member.role">
                    </UserCard>
                    <div class="add-member" @click="adding = true">
                        <font-awesome-icon class="icon" :icon="['fas', 'plus']"></font-awesome-icon>
                        Ajouter un membre
                    </div>
                </div>
            </div>
            <footer>
                <button class="primary" @click="create">Créer</button>
            </footer>
        </div>
    </main>
</template>

<script setup lang="ts">
import UserCard from '@/components/UserCard.vue';
import AddMember from '@/components/AddMember.vue';
import { extractUserFromSession } from '@/utils/session';
import { ref } from 'vue';
import { fetcher } from '@/utils/fetcher';
import { useRouter } from 'vue-router';
import type { ProjectErrors } from '@/validations/projectvalidation';
import { validateName, validateDescription } from '@/validations/projectvalidation';

const router = useRouter()

const name = ref()
const description = ref()
const members = ref<any[]>([])

const adding = ref(false)

const session = extractUserFromSession()
members.value.push({
    user: session?.user,
    role: 'Chef de projet'
})

function add(member: any) {
    if (member) {
        members.value.push(member)
    }
    adding.value = false
}

const errors = ref<ProjectErrors>({
    request: 'test'
})

async function create() {
    const nameValidation = validateName(name.value)
    errors.value.name = nameValidation
    const descriptionValidation = validateDescription(description.value)
    errors.value.description = descriptionValidation

    if (nameValidation || descriptionValidation) {
        return
    }

    const response = await fetcher('http://localhost:5000/projects', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name.value,
            description: description.value,
            members: members.value.map(member => {
                return {
                    id: member.user.id,
                    role: member.role
                }
            })
        })
    })

    if (response.status === 201) {
        const data = await response.json()
        router.push({
            name: 'project',
            params: {
                id: data.id
            }
        })
    }

    if (response.status >= 400 && response.status < 500) {
        errors.value.request = await response.text()
    }

    if (response.status >= 500) {
        errors.value.request = 'Une erreur est survenue'
    }
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

.add-member {
    padding: 8px;

    cursor: pointer;
}

.member {
    cursor: default;
}

.members {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
</style>