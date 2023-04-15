<template>
    <header v-if="session">
        <Notifications></Notifications>
        <div class="navigation">
            <RouterLink to="/">
                <font-awesome-icon class="icon navigation-item" :icon="['fas', 'house']" />
            </RouterLink>
            <RouterLink to="/discover">
                <font-awesome-icon class="icon navigation-item" :icon="['fas', 'compass']" />
            </RouterLink>

        </div>
        <div class="user-container" @click="toggle">
            <UserCard :user="session.user" navigate="no"></UserCard>
            <font-awesome-icon :icon="['fas', 'caret-down']" />
        </div>
        <div v-if="showDropdown" class="dropdown">
            <RouterLink @click="showDropdown = false" to="/me" class="dropdown-item">
                <font-awesome-icon class="icon" :icon="['fas', 'user']" />
                <span>Profile</span>
            </RouterLink>
            <div to="/logout" class="dropdown-item" @click="logout">
                <font-awesome-icon class="icon" :icon="['fas', 'sign-out-alt']" />
                <span>Logout</span>
            </div>
        </div>
    </header>
    <header v-else>
        <RouterLink to="/login">Login</RouterLink>
    </header>

    <MessageSidebar v-if="$route.path != '/login' && $route.path != '/register'" class="sidebar"></MessageSidebar>

    <RouterView />
</template>
  
<script setup lang="ts">
import UserCard from './components/UserCard.vue';
import { useRouter, RouterLink } from 'vue-router';
import { storeToRefs } from 'pinia'
import { useCookies } from 'vue3-cookies';
import { ref } from 'vue';
import { useSessionStore } from './stores/session';
import MessageSidebar from './components/messages/MessageSidebar.vue';
import Notifications from './components/Notifications.vue';

const router = useRouter()
const { cookies } = useCookies()
const store = useSessionStore()

const { session } = storeToRefs(store)
const { clearSession } = store

const showDropdown = ref(false)
function toggle() {
    showDropdown.value = !showDropdown.value
}

function logout() {
    showDropdown.value = false
    // Delete cookie and redirect to login
    cookies.set('token', '')
    clearSession()
    router.push('/login')
}
</script>
  
<style scoped>
header {
    color: #fffdfd;

    background-color: #692672;
    height: 64px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 0px 16px;
}

.user-container {
    display: flex;
    align-items: center;
    justify-content: center;

    gap: 16px;

    cursor: pointer;
}

.dropdown {
    color: #000;
    font-size: 24px;

    position: absolute;
    top: 64px;
    right: 16px;
    width: 200px;

    background-color: #fffdfd;
    border-radius: 8px;

    display: flex;
    flex-direction: column;
    gap: 8px;
}

.dropdown-item {
    padding: 16px;
    cursor: pointer;
}

.dropdown-item:hover {
    background-color: #e6e6e6;
}

.dropdown-item:active {
    background-color: #cccccc;
}

.icon {
    margin-right: 8px;
}

.sidebar {
    position: fixed;
    left: 0;
    bottom: 0;
    top: 50%;
    width: 400px;
}

.navigation {
    font-size: 28px;
    display: flex;
    gap: 16px;
    align-items: center;
}

.navigation-item {
    cursor: pointer;
}

.navigation-item:hover {
    color: #e6e6e6;
}
</style>
  