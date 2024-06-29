<template>
    <section class="levels">
        <section class="levels__board">
            <div class="levels__board__info-container">
                <div class="levels__board__info-container__info">
                    <h3>Module: {{ currentModule?.moduleName }}</h3>
                    <span>Progress: {{ progressPercentage }}%</span>
                </div>
            </div>
            <Level v-if="currentModule" :current-module="currentModule" v-bind="$attrs" />
        </section>

    </section>
    
</template>

<script setup lang="ts">
import { ComputedRef, Ref, computed, onMounted, ref } from 'vue';
import {  LevelsInterface } from '../interfaces/LevelsInterfaces';
import Level from './Level.vue';
import { ModulesEnum } from '../enums/ModulesEnum';
import { StatusEnum } from '../enums/StatusEnum';




const progress:Ref<number>=ref(0)
const progressPercentage:ComputedRef<number>=computed(()=>progress.value*100)
const currentModule:Ref<LevelsInterface | undefined> =ref()




const buildLevelInterface = ()=>{
    const storage = localStorage.getItem('levelsInterface') 
    if(!storage){
        currentModule.value={
            moduleName: 'Basic Phrases',
            moduleId:ModulesEnum.EASY,
            levels: [
                {step:1 ,status:StatusEnum.IN_PROGRESS},
                {step:2 ,status:StatusEnum.NOT_COMPLETED},
                {step:3 ,status:StatusEnum.NOT_COMPLETED},
                {step:4 ,status:StatusEnum.NOT_COMPLETED},
            ],
            isCompleted:false
        }
        return
       
    }
    const levelsInterface = JSON.parse(storage) as LevelsInterface
    currentModule.value={
        moduleName: levelsInterface.moduleName,
        moduleId: levelsInterface.moduleId,
        levels:levelsInterface.levels,
        isCompleted:levelsInterface.isCompleted
    }
    let progressCounter:number=0 ;
    levelsInterface.levels.forEach(ele=>{
        if(ele.status===StatusEnum.COMPLETED){
            progressCounter++
        }
    })
    if(!progressCounter) progress.value=0
    else progress.value=progressCounter/levelsInterface.levels.length

}



onMounted(()=>{
    buildLevelInterface()
})

</script>