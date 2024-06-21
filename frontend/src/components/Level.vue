<template>
    <section class="level-container">
        <div v-for="level in actualLevel.levels" :key="level.step" class="level-container__step" :class="level.status">
            <img :src="returnLevelIcon(level.status)"  />
        </div>
        <button :disabled="!actualLevel.isCompleted">NEXT</button>
    </section>
</template>

<script setup lang="ts">
import { PropType, Ref, ref } from "vue";
import {LevelsInterface} from "./../interfaces/LevelsInterfaces"
const props = defineProps({
    currentModule:{type:Object as PropType<LevelsInterface>,required:true}
})

const returnLevelIcon = (status:string)=>`src/assets/${status}.svg`

const actualLevel:Ref<LevelsInterface>=ref(props.currentModule)
    

</script>