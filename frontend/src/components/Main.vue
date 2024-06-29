<template>
  <main>
    <Settings v-if="props.view === SideBarEnum.SETTINGS" v-bind="$attrs" />
    <Levels
      v-else-if="props.view === SideBarEnum.LEVELS"
      @startLevel="startLevel"  v-bind="$attrs"
    />
    <Learn
      v-else-if="props.view === SideBarEnum.LEARN && currentLearnSession"
      :current-learn-session="currentLearnSession"  v-bind="$attrs"
    />
    <Authors v-else />
  </main>
</template>

<script setup lang="ts">
import Settings from "./Settings.vue";
import Levels from "./Levels.vue";
import Learn from "./Learn.vue";
import { SideBarEnum } from "../enums/SideBarEnum";
import { PropType, Ref, onMounted, ref } from "vue";
import { CurrentLearnSession } from "../interfaces/LearnInterfaces";
import { ModulesEnum } from "../enums/ModulesEnum";
import { StatusEnum } from "../enums/StatusEnum";
import Authors from "./Authors.vue"

const props = defineProps({
  view: { type: String as PropType<SideBarEnum>, required: true },
});

const currentLearnSession: Ref<CurrentLearnSession | undefined> = ref();





const startLevel = async (
  
  stepInfo: { step: number; moduleName: string; moduleId: ModulesEnum } = {
    step: 1,
    moduleName: "Basic Phrases",
    moduleId: ModulesEnum.EASY,
  }
) => {
  const texts = await getData(stepInfo.moduleId, stepInfo.step);
  currentLearnSession.value = {
    moduleName: stepInfo.moduleName,
    step: stepInfo.step,
    moduleId: stepInfo.moduleId,
    status: StatusEnum.IN_PROGRESS,
    texts: texts,
  };
};



const getData = async (
  currentModuleId: ModulesEnum,
  step: number = 1
) => {
  const module = currentModuleId ? currentModuleId : ModulesEnum.EASY;
  const result = await fetch("http://localhost:8000/getDataByLevel", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      level: module,
    }),
  })
    .then((res) => res.json())
    .catch((err) => err);
  let rangeStart: number;
  let rangeEnd: number;

  switch (step) {
    case 1:
      rangeStart = 0;
      rangeEnd = 3;
      break;
    case 2:
      rangeStart = 3;
      rangeEnd = 6;
      break;
    case 3:
      rangeStart = 6;
      rangeEnd = 9;
      break;
    case 4:
      rangeStart = 9;
      rangeEnd = 12;
      break;
    default:
      throw new Error("Invalid rangeId");
  }

  const filteredResult = result.slice(rangeStart, rangeEnd);
  return filteredResult;
};
onMounted(async()=>{
  const learnSession = localStorage.getItem("currentLearnSession")
  if(learnSession) currentLearnSession.value = JSON.parse(learnSession) 
  await startLevel(currentLearnSession.value)
})
</script>
