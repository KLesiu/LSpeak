<template>
    <main>
        <Settings  v-if="props.view === SideBarEnum.SETTINGS" v-bind="$attrs" />
        <Levels  v-else-if="props.view === SideBarEnum.LEVELS" />
    </main>
</template>

<script setup lang="ts">
import Settings from './Settings.vue';
import Levels from './Levels.vue';
import { SideBarEnum } from '../enums/SideBarEnum';
import { PropType } from 'vue';

const props = defineProps({
    view:{type:String as PropType<SideBarEnum>,required:true}
})




</script>