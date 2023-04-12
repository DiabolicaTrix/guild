<template>
    <div v-if="editing" class="input">
        <input type="text" v-model="value" />
        <font-awesome-icon class="icon clickable" :icon="['fas', 'check']"
            @click="editing = false; $emit('submit', value)"></font-awesome-icon>
    </div>
    <div v-else class="input">
        <h2>{{ value }}</h2>
        <font-awesome-icon class="icon show-on-hover clickable" :icon="['fas', 'edit']"
            @click="editing = true"></font-awesome-icon>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const emit = defineEmits(['submit'])
const props = defineProps(['value'])

const value = ref(props.value)
const editing = ref(false)
</script>

<style scoped>
.input {
    display: flex;
    align-items: center;
    gap: 8px;
}

.input:hover .show-on-hover {
    visibility: visible;
}

.show-on-hover {
    visibility: hidden;
}
</style>

