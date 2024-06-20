<script setup lang="ts"></script>

<template>
  <aside>
    <div class="main-tabs">
      <div class="main-tabs__menu-tab">
        <img src="./../assets//learn.svg" alt="" />
        <span>Learn</span>
      </div>
      <div class="main-tabs__menu-tab">
        <img src="./../assets//levels.svg" alt="" />
        <span>Levels</span>
      </div>
      <div class="main-tabs__menu-tab">
        <img src="./../assets//settings.svg" alt="" />
        <Span>Settings</Span>
      </div>
    </div>
    <div class="authors-tab main-tabs__menu-tab">
      <img src="./../assets//authors.svg" alt="" />
      <span>Authors</span>
    </div>
  </aside>
</template>

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
    }
  }
  .authors-tab {
    color: #f8f8f8;
    background-color: #e60060;
  }
}
</style>
