<template>
    <section class="levels">
        <section class="levels__board">
            <div class="levels__board__info-container">
                <div class="levels__board__info-container__info">
                    <h3>Module: {{ moduleName }}</h3>
                    <span>Progress: {{ progressPercentage }}%</span>
                </div>
            </div>
            <Level :current-module="levelsDB" />
        </section>

    </section>
    
</template>

<script setup lang="ts">
import { ComputedRef, Ref, computed, ref } from 'vue';
import Level from './Level.vue';
import { LevelsInterface } from '../interfaces/LevelsInterfaces';
import { ModulesEnum } from '../enums/ModulesEnum';
import { StatusEnum } from '../enums/StatusEnum';


const moduleName:Ref<string> = ref('Basic Phrases');
const progress:Ref<number>=ref(0)
const progressPercentage:ComputedRef<number>=computed(()=>progress.value*100)


const levelsDB:LevelsInterface = {
    moduleName: 'Basic Phrases',
    moduleId:ModulesEnum.EASY,
    levels: [
        {step:1 ,status:StatusEnum.COMPLETED},
        {step:2 ,status:StatusEnum.COMPLETED},
        {step:3 ,status:StatusEnum.IN_PROGRESS},
        {step:4 ,status:StatusEnum.NOT_COMPLETED},
    ],
    isCompleted:false

}

</script>