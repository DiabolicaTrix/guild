<template>
    <div class="notifications-button clickable" @click="show = !show">
        <font-awesome-icon :icon="['fas', 'bell']" />
        <div v-if="notifications.length > 0" class="bell-pin"></div>
    </div>
    <div v-if="show" class="dropdown">
        <div v-for="notification in notifications" class="dropdown-item clickable">
            <span>{{ notification.message }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">
import { fetcher } from '@/utils/fetcher';
import { extractUserFromSession } from '@/utils/session';
import { ref } from 'vue';

const session = extractUserFromSession()
const userId = session?.user.id

const show = ref(false)

const notifications = ref<any[]>([
    {
        from: {
            id: 1,
            name: 'John Doe',
            picture: 'https://picsum.photos/200/300'
        },
        message: 'John Doe a appliqué pour votre projet',
    }
])
fetcher(`http://localhost:5000/users/${userId}/notifications`)
    .then(response => response.json())
    .then(data => {
        notifications.value = data;
    })

</script>

<style scoped>
.notifications-button {
    font-size: 28px;

    position: relative;
}

.bell-pin {
    position: absolute;
    top: 85%;
    right: -10%;

    width: 8px;
    height: 8px;

    background-color: #ff0000;
    border-radius: 50%;
}

.dropdown {
    position: absolute;
    top: 64px;
    left: 0;

    width: 300px;
    height: 300px;

    background-color: #FFFDFD;
    border-radius: 8px;
    border: 1px solid rgba(0, 0, 0, 0.2);

    overflow-y: scroll;
}

.dropdown-item {
    padding: 8px 16px;
    color: black;
}
</style>