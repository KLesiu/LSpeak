<template>
    <menu>
        <button @click="setActiveTab(MenuTabsEnum.SOUNDS)"  :class="{'active': activeTab === MenuTabsEnum.SOUNDS}">Sounds</button>
        <button @click="setActiveTab(MenuTabsEnum.LANG)" :class="{'active' :activeTab === MenuTabsEnum.LANG}">Languages</button>
    </menu>
</template>

<script setup lang="ts">
import { Ref, ref } from "vue";
import {MenuTabsEnum} from "./../enums/MenuTabsEnum"

const emits =  defineEmits(["activeTab"])
const activeTab:Ref<MenuTabsEnum>=ref(MenuTabsEnum.SOUNDS);

const setActiveTab=(tab:MenuTabsEnum):void=>{
    activeTab.value=tab;
    emits("activeTab",activeTab.value)
}
</script>