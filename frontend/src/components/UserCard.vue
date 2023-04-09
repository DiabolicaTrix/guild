<template>
    <div @click="click" :class="user.id ? 'user clickable' : 'user'">
        <img class="avatar" :src="props.user.picture" />
        <div class="user-details">
            <h2>{{ props.user.name }}</h2>
            <h3 v-if="props.subtitle">{{ props.subtitle }}</h3>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const props = defineProps(['user', 'subtitle', 'navigate'])

const user = ref(props.user)
if (!props.user) {
    user.value = {
        name: 'Vacant',
        picture: '/avatar-placeholder.png'
    }
}

function click() {
    if (props.navigate === 'no') {
        return
    }

    if (!user.value.id) {
        return
    }
    router.push({ name: 'user', params: { id: user.value.id } })
}
</script>

<style scoped>
.clickable {
    cursor: pointer;
}

.user-details {
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: center;
}

h2 {
    font-weight: bold;
}
</style>
