<template>
    <section class="level-container">
        <div v-for="level in actualLevel.levels" :key="level.step" class="level-container__step" :class="level.status">
            <img :src="returnLevelIcon(level.status)" @click="startLevel(level.step,level.status)"  />
        </div>
    </section>
</template>

<script setup lang="ts">
import { PropType, Ref, ref } from "vue";
import {LevelsInterface} from "./../interfaces/LevelsInterfaces"
import { StatusEnum } from "../enums/StatusEnum";
const props = defineProps({
    currentModule:{type:Object as PropType<LevelsInterface>,required:true}
})
const emits = defineEmits(['startLevel'])

const returnLevelIcon = (status:string)=>`src/assets/${status}.svg`

const actualLevel:Ref<LevelsInterface>=ref(props.currentModule)
    

const startLevel = (step:number,status:StatusEnum)=>{
    if(status!==StatusEnum.IN_PROGRESS) return
    const stepInfo = {
        step: step,
        moduleName:props.currentModule.moduleName,
        moduleId:props.currentModule.moduleId
    }
    emits('startLevel',stepInfo)
}

</script>