<template>
    <div class="wrapper post-input">
        <textarea placeholder="Décrivez l'avancée du projet" :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"></textarea>
        <button v-if="!props.loading" class="primary" @click="submit">Publier</button>
        <button v-else class="primary">
            <sync-loader color="#fffdfd" size="8px"></sync-loader>
        </button>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps(['loading', 'modelValue'])
const emit = defineEmits(['submit', 'update:modelValue'])

function submit() {
    emit('submit')
}
</script>

<style scoped>
.post-content {
    padding: 0px 16px 16px 16px;
    text-align: justify;
}

.post-input {
    padding: 16px;

    display: flex;
    flex-direction: column;
    gap: 16px;
}

textarea {
    width: 100%;
    height: 100px;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px 8px;
    box-sizing: border-box;
    resize: none;

    font-family: 'Roboto', sans-serif;
    font-size: 18px;
}
</style>