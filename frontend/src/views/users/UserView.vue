<template>
  <main>
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
            <button class="primary">Contacter</button>
          </div>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="portfolio">
        <h1>Projects</h1>
        <div class="projects-container">
          <carousel :items-to-show="2.5" class="carousel">
            <slide v-for="project in projects" :key="project.id">
              <ProjectCard :value="project"></ProjectCard>
            </slide>
          </carousel>
        </div>
      </div>
      <div class="content">
        <Post v-for="post in posts" :post="post"></Post>
      </div>
    </div>

  </main>
</template>

<script setup lang="ts">
import ProjectCard from '@/components/ProjectCard.vue';
import Post from '@/components/Post.vue';

import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide } from 'vue3-carousel'

import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { fetcher } from '@/utils/fetcher';

const route = useRoute()

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
  top: 50%;
  margin-top: -93px;

  left: 50%;
  margin-left: -93px;
}

.profile-picture {
  height: 170px;
  width: 170px;
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
}

.carousel {
  width: 100%;
}
</style>
