<template>
    <section class="learn">
        <div class="learn__header">
            <div>
                <h2>Module: {{ currentLearnSession.moduleName }}</h2>
                <span>Step: {{ currentLearnSession.step }}</span>
            </div>
            <div class="learn__header__timer">
                <span :class="{'expiring': timer < 10}">{{ timer }}s</span>
                <Hourglass />
            </div>
            
        </div>
        <div class="learn__main">
            <div class="learn__main__baseLang">
                <img :src="returnBaseLangImage()" />
                <span>Jak sie masz?</span>
            </div>
            <div class="learn__main__microphoneContainer">
                <img class="learn__main__microphoneContainer__micro" @click="toggleMicro" :src="returnMicroImage" />
                <img class="learn__main__microphoneContainer__lang" :src="returnSecondLangImage()" />
            </div>
            <div class="learn__main__resultContainer">
                <div class="learn__main__resultContainer__result">
                    <img :src="returnSecondLangImage()" />
                    <span>Haw they you?</span>
                </div>
                <span class="learn__main__resultContainer__correctAnswer">How are you?</span>
            </div>
        </div>
    </section>
</template>


<script lang="ts" setup>
import { PropType, Ref, computed, ref } from 'vue';
import {CurrentLearnSession} from "./../interfaces/LearnInterfaces"
import Hourglass from './Hourglass.vue';


const props = defineProps({
    currentLearnSession:{type:Object as PropType<CurrentLearnSession>,required:true}
})

const isMicrophoneActive:Ref<boolean> = ref(false)

const configLang = JSON.parse(localStorage.getItem("configLang")!)
const timer:Ref<number> = ref(90)

const returnBaseLangImage = ()=>`/src/assets/${configLang.baseLang}.svg`
const returnSecondLangImage = ()=> `/src/assets/${configLang.secondLang}.svg`
const returnMicroImage = computed(()=>isMicrophoneActive.value ? "/src/assets/micro-active.svg" : "/src/assets/micro.svg"    )

const toggleMicro = ():void=>{
    isMicrophoneActive.value = !isMicrophoneActive.value
}

setInterval(()=>{
    timer.value--
},1000)

</script>