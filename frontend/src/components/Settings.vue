<template>
    <section class="settings">
        <h2>Settings</h2>
        <MenuTabs @active-tab="setActiveView" />
        <SoundsSettings v-if="currentView === MenuTabsEnum.SOUNDS" />
        <LanguagesSettings v-else-if="currentView === MenuTabsEnum.LANG" v-bind="$attrs" />
    </section>
</template>

<script setup lang="ts">
import { Ref, ref } from "vue";
import { MenuTabsEnum } from "../enums/MenuTabsEnum";
import MenuTabs from "./MenuTabs.vue";
// import SoundsSettings from "./SoundsSettings.vue";
import LanguagesSettings from "./LanguagesSettings.vue";


const currentView: Ref<MenuTabsEnum> = ref(MenuTabsEnum.SOUNDS);

const setActiveView = (tabName: MenuTabsEnum): void => {
   switch (tabName) {
      case MenuTabsEnum.SOUNDS:
         currentView.value = MenuTabsEnum.SOUNDS;
         break;
      case MenuTabsEnum.LANG:
        currentView.value = MenuTabsEnum.LANG;
         break;
   }
};

</script>