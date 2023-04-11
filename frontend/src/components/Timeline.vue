<template>
    <div class="timeline-wrapper">
        <div class="timeline">
            <img src="/progressbar-background.svg" />
            <img class="front" src="/progressbar-front.svg" />
        </div>
    </div>
</template>

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
    width: calc(673px * 0.5);
    margin-left: 5px;
    margin-top: 5px;

}
</style>