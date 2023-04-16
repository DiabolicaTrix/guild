<template>
  <main v-if="user">
    <div class="sidebar">
      <div class="profile">
        <div class="profile-background"></div>
        <div class="profile-picture-wrapper">
          <img class="profile-picture" :src="user.picture" />
        </div>
        <div class="info">
          <div class="name">
            <h1>{{ user.name }}</h1>
            <h2>{{ user.role }}</h2>
          </div>
          <div class="actions">
            <button class="primary" @click="contact">Contacter</button>
          </div>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="portfolio">
        <h1>Projects</h1>
        <div class="projects-container">
          <div v-for="project in projects">
            <ProjectCard :value="project"></ProjectCard>
          </div>
        </div>
      </div>
      <div class="content">
        <Post v-for="post in posts" :post="post"></Post>
      </div>
    </div>

  </main>
  <main v-else>
    <div class="error">Cet utilisateur n'existe pas</div>
  </main>
</template>

<script setup lang="ts">
import ProjectCard from '@/components/ProjectCard.vue';
import Post from '@/components/Post.vue';


import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { fetcher } from '@/utils/fetcher';
import { useMessaging } from '@/stores/messaging';
import { extractUserFromSession } from '@/utils/session';

const route = useRoute()
const router = useRouter()
const messaging = useMessaging()

const session = extractUserFromSession()
if (session?.user.id == route.params.id) {
  router.push('/me')
}

const user = ref()
fetcher(`http://localhost:5000/users/${route.params.id}`)
  .then(response => response.json())
  .then(data => {
    user.value = data;
  })

const posts = ref()
fetcher(`http://localhost:5000/users/${route.params.id}/posts`)
  .then(response => response.json())
  .then(data => {
    posts.value = data;
  })

const projects = ref()
fetcher(`http://localhost:5000/users/${route.params.id}/projects`)
  .then(response => response.json())
  .then(data => {
    projects.value = data;
  })

function contact() {
  messaging.open(user.value)
}
</script>

<style scoped>
main {
  display: flex;
  justify-content: center;

  margin-top: 36px;
  gap: 36px;
}

.sidebar {
  display: flex;

  flex-direction: column;
  gap: 26px;
}

.content {
  width: 800px;
  display: flex;
  flex-direction: column;

  gap: 36px;
}

.profile {
  background-color: #FFFDFD;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0.2);

  width: 400px;
  height: 387px;

  position: relative;
}

.profile-background {
  background-color: #e3a0e4;
  border-radius: 8px 8px 0 0;

  height: 200px;
}

.profile-picture-wrapper {
  background-color: #fffdfd;
  border-radius: 93px;

  width: 186px;
  height: 186px;

  display: flex;
  justify-content: center;
  align-items: center;

  position: absolute;
  top: 50%;
  margin-top: -93px;

  left: 50%;
  margin-left: -93px;
}

.profile-picture {
  height: 170px;
  width: 170px;

  border-radius: calc(170px / 2);
}

.info {
  position: absolute;
  bottom: 16px;

  padding: 0 16px 0 32px;

  width: 100%;

  display: flex;
  justify-content: space-between;
  align-items: end;
}

.portfolio {
  background-color: #FFFDFD;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0.2);

  width: 800px;

  padding: 28px 32px;

  display: flex;
  flex-direction: column;
  gap: 12px
}

.projects-container {
  display: flex;
  gap: 32px;

  overflow-x: scroll;
}

.projects-container::-webkit-scrollbar {
  display: none;
}
</style>
