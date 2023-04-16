<template>
    <div class="wrapper" @click="click">
        <img v-if="props.value.pictures && props.value.pictures[0]" :src="props.value.pictures[0]" />
        <div class="info">
            <h4>{{ props.value.name }}</h4>
            <p>{{ props.value.description }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import router from '@/router';

const props = defineProps(['value'])

function click() {
    router.push({ name: 'project', params: { id: props.value.id } })
}
</script>

<style scoped>
.wrapper {
    height: auto;
    width: 224px;

    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    background-color: #fffdfd;

    cursor: pointer;
}

img {
    width: 100%;
    height: 175px;
    border-radius: 8px 8px 0 0;
}

.info {
    display: flex;
    flex-direction: column;
    align-items: start;

    padding: 4px 8px;
}
</style>