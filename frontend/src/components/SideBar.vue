<template>
  <aside>
    <div class="main-tabs">
      <div
        class="main-tabs__menu-tab"
        :class="{ active: activeTab === SideBarEnum.LEARN }"
        @click="setActiveTab(SideBarEnum.LEARN)"
      >
        <img src="./../assets/learn.svg" alt="Learn Icon" />
        <span>Learn</span>
      </div>
      <div
        class="main-tabs__menu-tab"
        :class="{ active: activeTab === SideBarEnum.LEVELS }"
        @click="setActiveTab(SideBarEnum.LEVELS)"
      >
        <img src="./../assets/levels.svg" alt="Levels Icon" />
        <span>Levels</span>
      </div>
      <div
        class="main-tabs__menu-tab"
        :class="{ active: activeTab === SideBarEnum.SETTINGS }"
        @click="setActiveTab(SideBarEnum.SETTINGS)"
      >
        <img src="./../assets/settings.svg" alt="Settings Icon" />
        <span>Settings</span>
      </div>
    </div>
    <div class="authors-tab main-tabs__menu-tab" @click="setActiveTab(SideBarEnum.AUTHORS)">
      <img src="./../assets/authors.svg" alt="Authors Icon" />
      <span>Authors</span>
    </div>
  </aside>
</template>

<script setup lang="ts">
import {SideBarEnum} from "./../enums/SideBarEnum";
import { ref } from "vue";

const activeTab = ref<SideBarEnum>(SideBarEnum.LEVELS);
const emits = defineEmits(["activeTab"]);

const setActiveTab = (tab: SideBarEnum) => {
  activeTab.value = tab;
  emits('activeTab',tab);
};
</script>
