<template>
  <main>
    <div class="content">
      <Post v-for="post in posts" :post="post"></Post>
    </div>
  </main>
</template>

<script setup lang="ts">
import Post from '@/components/Post.vue';
import { fetcher } from '@/utils/fetcher';
import { ref } from 'vue';
import 'vue3-carousel/dist/carousel.css'

const posts = ref()
fetcher(`http://localhost:5000/posts`)
  .then(response => response.json())
  .then(data => {
    posts.value = data;
  })

</script>

<style scoped>
main {
  display: flex;
  justify-content: center;

  margin-top: 36px;
}

.content {
  width: 800px;

  display: flex;
  flex-direction: column;
  gap: 36px;
}
</style>
