<template>
  <aside>
    <div class="main-tabs">
      <div
        class="main-tabs__menu-tab"
        :class="{ active: activeTab === 'learn' }"
        @click="setActiveTab('learn')"
      >
        <img src="./../assets/learn.svg" alt="Learn Icon" />
        <span>Learn</span>
      </div>
      <div
        class="main-tabs__menu-tab"
        :class="{ active: activeTab === 'levels' }"
        @click="setActiveTab('levels')"
      >
        <img src="./../assets/levels.svg" alt="Levels Icon" />
        <span>Levels</span>
      </div>
      <div
        class="main-tabs__menu-tab"
        :class="{ active: activeTab === 'settings' }"
        @click="setActiveTab('settings')"
      >
        <img src="./../assets/settings.svg" alt="Settings Icon" />
        <span>Settings</span>
      </div>
    </div>
    <div class="authors-tab main-tabs__menu-tab">
      <img src="./../assets/authors.svg" alt="Authors Icon" />
      <span>Authors</span>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { ref } from "vue";

const activeTab = ref<string | null>(null);

const setActiveTab = (tab: string) => {
  activeTab.value = tab;
};
</script>

<style scoped lang="scss">
aside {
  background-color: rgba(255, 255, 255, 0.768627451);
  font-weight: 500;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 80px 0 0 0;
  width: 90px;
  height: 100vh;
  .main-tabs {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    &__menu-tab {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 1rem 0.5rem;
      cursor: pointer;
      gap: 0.5rem;
      &.active {
        color: #e50060;
        img {
          filter: invert(31%) sepia(99%) saturate(2647%) hue-rotate(320deg)
            brightness(91%) contrast(101%);
        }
      }
    }
  }
  .authors-tab {
    color: #f8f8f8;
    background-color: #e60060;
  }
}
</style>

<!-- <style scoped lang="scss">
aside {
  background-color: rgba(255, 255, 255, 0.768627451);
  font-weight: 500;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 80px 0 0 0;
  width: 90px;
  height: 100vh;
  .main-tabs {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    &__menu-tab {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 1rem 0.5rem;
      cursor: pointer;
      gap: 0.5rem;
    }
  }
  .authors-tab {
    color: #f8f8f8;
    background-color: #e60060;
  }
}
</style> -->
