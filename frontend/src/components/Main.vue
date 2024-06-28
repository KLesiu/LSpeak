<template>
  <main>
    <Settings v-if="props.view === SideBarEnum.SETTINGS" v-bind="$attrs" />
    <Levels v-else-if="props.view === SideBarEnum.LEVELS" />
    <Learn
      v-else-if="props.view === SideBarEnum.LEARN"
      :current-learn-session="fake"
    />
    <Authors v-else-if="props.view === SideBarEnum.AUTHORS" />
  </main>
</template>

<script setup lang="ts">
import Authors from "./Authors.vue";
import Settings from "./Settings.vue";
import Levels from "./Levels.vue";
import Learn from "./Learn.vue";
import { SideBarEnum } from "../enums/SideBarEnum";
import { PropType } from "vue";
import { CurrentLearnSession } from "../interfaces/LearnInterfaces";
import { ModulesEnum } from "../enums/ModulesEnum";
import { StatusEnum } from "../enums/StatusEnum";

const props = defineProps({
  view: { type: String as PropType<SideBarEnum>, required: true },
});

const fake: CurrentLearnSession = {
  moduleName: "Basic Phrases",
  step: 1,
  moduleId: ModulesEnum.EASY,
  status: StatusEnum.IN_PROGRESS,
  texts: [],
};
</script>
