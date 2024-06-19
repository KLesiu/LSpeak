<template>
    <SideBar />
    <section class="main-container">
        <Header :langSet="langSet" />
        <Main @set-lang-set="setLangSet"/>
    </section>

    
</template>

<script setup lang="ts">
import SideBar from './components/SideBar.vue'
import Header from './components/Header.vue'
import Main from "./components/Main.vue"
import { LanguagesSetEnum } from './enums/LanguagesEnum';
import { Ref, onMounted, ref } from 'vue';

const langSet:Ref<LanguagesSetEnum> = ref(LanguagesSetEnum.POLEN);

const setLangSet = (newlangSet:LanguagesSetEnum):void=>{
    langSet.value=newlangSet;
}

onMounted(()=>{
    const langSetFromLocalStorage=localStorage.getItem("langSet");
    if(!langSetFromLocalStorage)return;
    langSet.value=langSetFromLocalStorage as LanguagesSetEnum;
})


</script>

