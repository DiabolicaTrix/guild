<template>
    <div class="picture-container">
        <img class="profile-picture clickable" :src="props.path ?? '/avatar-placeholder.png'" />
        <font-awesome-icon class="icon edit-icon" :icon="['fas', 'pen-to-square']" />
    </div>
</template>

<script setup lang="ts">
const props = defineProps(['path'])

</script>

<style scoped>
.picture-container {
    cursor: pointer;
}

.picture-container:hover .profile-picture {
    filter: brightness(0.8);
}

.picture-container:hover .edit-icon {
    visibility: visible;
}

.profile-picture {
    height: 170px;
    width: 170px;

    border-radius: calc(170px / 2);
}

.edit-icon {
    color: #fffdfd;
    visibility: hidden;
    position: absolute;
    font-size: 32px;
}
</style>
