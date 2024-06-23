<template>
    <section class="learn">
        <div class="learn__header">
            <div>
                <h2>Module: {{ currentLearnSession.moduleName }}</h2>
                <span>Step: {{ currentLearnSession.step }}</span>
            </div>
            <div class="learn__main">
                <span>{{ timer }}s</span>
                <Hourglass />
            </div>
            
        </div>

    </section>
</template>


<script lang="ts" setup>
import { PropType, Ref, ref } from 'vue';
import {CurrentLearnSession} from "./../interfaces/LearnInterfaces"
import Hourglass from './Hourglass.vue';


const props = defineProps({
    currentLearnSession:{type:Object as PropType<CurrentLearnSession>,required:true}
})

const timer:Ref<number> = ref(90)

setInterval(()=>{
    timer.value--
},1000)

</script>