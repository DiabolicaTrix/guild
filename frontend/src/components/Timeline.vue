<template>
    <div class="timeline-wrapper">
        <div class="timeline">
            <img src="/progressbar-background.svg" />
            <img :style="getProgress" class="front" src="/progressbar-front.svg" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
    progress: number;
}>();

const getProgress = computed(() => {
    return {
        width: `${props.progress / 100 * 673}px`
    }
})

</script>

<style scoped>
.timeline-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

.timeline {
    width: 683px;
    height: 62px;
}

img {
    position: absolute;
    border-radius: 8px;

    object-fit: none;
    object-position: 0% 0;
}

img.front {
    height: 52px;
    margin-left: 5px;
    margin-top: 5px;

}
</style>