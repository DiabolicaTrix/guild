<template>
    <main>
        <div class="project" v-if="project">
            <carousel v-if="project.pictures" :items-to-show="1">
                <slide v-for="image in project.pictures" :key="project.name">
                    <img class="header" :src="image" />
                </slide>
                <template #addons>
                    <navigation />
                </template>
            </carousel>
            <div class="info">
                <h1>{{ project.name }}</h1>
                <span></span>
                <p>{{ project.description }}</p>
            </div>
            <Divider />
            <div class="members">
                <h1>Membres</h1>
                <span></span>
                <div class="members-wrapper" v-if="roles">
                    <div v-for="role in roles" class="member">
                        <UserCard :user="role.user ?? { name: 'Vacant', picture: '/avatar-placeholder.png' }"
                            :subtitle="role.name"></UserCard>
                        <button v-if="!role.user" class="apply primary">Appliquer</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="content">
            <Timeline class="wrapper milestone-wrapper"></Timeline>
            <PostInput v-if="roles && canPost()" v-model="postContent" @submit="publishPost" :loading="loading"></PostInput>
            <Post v-for="post in posts" :post="post"></Post>
        </div>

    </main>
</template>

<script setup lang="ts">
import Divider from '@/components/Divider.vue';
import Post from '@/components/Post.vue';
import PostInput from '@/components/PostInput.vue';
import Timeline from '@/components/Timeline.vue';
import UserCard from '@/components/UserCard.vue';
import { Carousel, Slide, Navigation } from 'vue3-carousel'

import { ref } from 'vue';
import { useRoute } from 'vue-router'
import { fetcher } from '@/utils/fetcher';
import { useSessionStore } from '@/stores/session';

const route = useRoute();
const { session } = useSessionStore();

const project = ref()
fetcher(`http://localhost:5000/projects/${route.params.id}`)
    .then(response => response.json())
    .then(data => {
        project.value = data;
    })

const posts = ref()

async function loadPosts() {
    await fetcher(`http://localhost:5000/projects/${route.params.id}/posts`)
        .then(response => response.json())
        .then(data => {
            posts.value = data;
        })
}
loadPosts()


const roles = ref()
fetcher(`http://localhost:5000/projects/${route.params.id}/roles`)
    .then(response => response.json())
    .then(data => {
        roles.value = data;
    })

function canPost() {
    console.log(roles.value)
    return roles.value.some((role: any) => role.user?.id === session.user.id)
}

const postContent = ref('')
const loading = ref(false)
async function publishPost() {
    console.log(postContent.value)
    loading.value = true;
    const response = await fetcher(`http://localhost:5000/posts`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            content: postContent.value,
            project_id: route.params.id,
        })
    })
    await loadPosts()

    if (response.status === 201) {
        postContent.value = ''
    }

    loading.value = false
}

</script>

<style scoped>
main {
    display: flex;
    justify-content: center;
    gap: 36px;

    margin-top: 36px;
}

.wrapper {
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    background-color: #fffdfd;
}

img.header {
    width: 100%;
    height: 300px;
    border-radius: 8px 8px 0 0;
}

span {
    display: block;
    height: 10px;
}

.project {
    width: 400px;
    height: 100%;

    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    background-color: #fffdfd;
}

.info {
    padding: 16px;
    text-align: justify;
}

.content {
    width: 800px;

    display: flex;
    flex-direction: column;
    gap: 36px;
}


.milestone-wrapper {
    height: 200px;
}

h2 {
    font-size: 18px;
    font-weight: bold;
}

.members {
    padding: 16px;
}

.members-wrapper>* {
    margin-top: 8px;
}

.members-wrapper>*:first-child {
    margin-top: 0px;
}

.member {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.apply {
    height: 28px;
    width: auto;
    padding: 4px 12px;
}
</style>