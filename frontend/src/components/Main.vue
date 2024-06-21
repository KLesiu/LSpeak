<template>
    <main>
        <Settings  v-if="false" v-bind="$attrs" />
        <Levels  />
    </main>
</template>

<script setup lang="ts">
import Settings from './Settings.vue';
import Levels from './Levels.vue';
</script>