<template>
  <SideBar @active-tab="setActiveTab" />
  <section class="main-container">
    <Header :langSet="langSet" />
    <Main @set-lang-set="setLangSet" :view="currenTabComp" />
  </section>
</template>

<script setup lang="ts">
import SideBar from "./components/SideBar.vue";
import Header from "./components/Header.vue";
import Main from "./components/Main.vue";
import { LanguagesSetEnum } from "./enums/LanguagesEnum";
import { ComputedRef, Ref, computed, onMounted, ref } from "vue";
import { SideBarEnum } from "./enums/SideBarEnum";

const langSet: Ref<LanguagesSetEnum> = ref(LanguagesSetEnum.POLEN);
const currentTab: Ref<SideBarEnum> = ref(SideBarEnum.AUTHORS);
const currenTabComp: ComputedRef<SideBarEnum> = computed(
  () => currentTab.value
);

const setLangSet = (newlangSet: LanguagesSetEnum): void => {
  langSet.value = newlangSet;
};

const setActiveTab = (tab: SideBarEnum): void => {
  currentTab.value = tab;
};

onMounted(() => {
  const langSetFromLocalStorage = localStorage.getItem("langSet");
  if (!langSetFromLocalStorage) return;
  langSet.value = langSetFromLocalStorage as LanguagesSetEnum;
});
</script>
