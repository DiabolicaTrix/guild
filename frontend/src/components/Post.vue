<template>
    <div class="wrapper">
        <div class="post">
            <div class="post-header">
                <UserCard :user="props.post.author"></UserCard>
                <h6>{{ formatDate(props.post.created_at) }}</h6>
            </div>
        </div>
        <div class="post-content">
            <p>{{ props.post.content }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import UserCard from './UserCard.vue';
import { DateTime } from 'luxon'

const props = defineProps(['post'])

function formatDate(date: string) {
    return DateTime.fromHTTP(date).toLocaleString(DateTime.DATETIME_MED)
}
</script>

<style scoped>
.post-content {
    padding: 0px 16px 16px 16px;
    text-align: justify;
}

.post-header {
    padding: 16px;

    display: flex;
    align-items: center;
    justify-content: space-between;
}
</style>