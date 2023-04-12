<template>
  <main>
    <div class="sidebar">
      <div class="profile" v-if="user">
        <div class="profile-background"></div>
        <EditableProfilePicture class="profile-picture-wrapper" :path="user.picture"></EditableProfilePicture>
        <div class="info">
          <div class="name">
            <h1>{{ user.name }}</h1>
            <EditableField :value="user.role" @submit="updateRole"></EditableField>
          </div>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="portfolio">
        <h1>Projects</h1>
        <div class="projects-container">
          <div v-for="project in [...projects, ...projects]">
            <ProjectCard :value="project"></ProjectCard>
          </div>
          <div class="create-project" @click="$router.push({ name: 'project-create' })">
            <font-awesome-icon class="icon" :icon="['fas', 'plus']"></font-awesome-icon>
            Ajouter un projet
          </div>
        </div>
      </div>
      <div class="content" v-if="posts">
        <Post v-for="post in posts" :post="post"></Post>
      </div>
    </div>

  </main>
</template>

<script setup lang="ts">
import Divider from '@/components/Divider.vue';
import ProjectCard from '@/components/ProjectCard.vue';
import EditableProfilePicture from '@/components/EditableProfilePicture.vue';
import EditableField from '@/components/EditableField.vue';
import Post from '@/components/Post.vue';

import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide } from 'vue3-carousel'

import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { fetcher } from '@/utils/fetcher';
import { useMessaging } from '@/stores/messaging';
import { extractUserFromSession } from '@/utils/session';

const messaging = useMessaging()

const session = extractUserFromSession()
const userId = session?.user.id

const user = ref()
fetcher(`http://localhost:5000/users/${userId}`)
  .then(response => response.json())
  .then(data => {
    user.value = data;
  })

const posts = ref()
fetcher(`http://localhost:5000/users/${userId}/posts`)
  .then(response => response.json())
  .then(data => {
    posts.value = data;
  })

const projects = ref()
fetcher(`http://localhost:5000/users/${userId}/projects`)
  .then(response => response.json())
  .then(data => {
    projects.value = data;
  })

function updateRole(role: string) {
  user.role.value = role
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
  left: 50%;
  top: calc(200px - 93px);
  transform: translate(-50%, 0);
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

  width: 687px;

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

.carousel {
  width: 100%;
}

.create-project {
  height: 275px;
  width: 224px;

  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  background-color: #fffdfd;

  cursor: pointer;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 8px;

  font-size: 24px;
}
</style>
