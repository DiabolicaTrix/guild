<template>
    <main>
        <AddMember v-if="adding" @add="add" />
        <div class="project wrapper">
            <header>
                <h1>Créer un projet</h1>
            </header>
            <div class="inputs">
                <label for="name">Nom du projet</label>
                <input type="text" name="name" v-model="name" />
                <label for="description">Description du projet</label>
                <textarea name="description" v-model="description"></textarea>
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
                <button class="primary">Créer</button>
            </footer>
        </div>
    </main>
</template>

<script setup lang="ts">
import UserCard from '@/components/UserCard.vue';
import AddMember from '@/components/AddMember.vue';
import { extractUserFromSession } from '@/utils/session';
import { ref } from 'vue';

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