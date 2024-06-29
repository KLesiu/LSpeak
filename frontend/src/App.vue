<template>
    <SideBar @active-tab="setActiveTab" :active="currenTabComp" />
    <section class="main-container">
        <Header v-if="isHeaderShow" :langSet="langSet" />
        <Main v-if="isMainShow && currenTabComp" @set-lang-set="setLangSet" @exit-to-levels="setActiveTab(SideBarEnum.LEVELS)" @level-completed="levelCompleted" :view="currenTabComp" @start-level="setActiveTab(SideBarEnum.LEARN)"/>
    </section>

    
</template>

<script setup lang="ts">
import SideBar from './components/SideBar.vue'
import Header from './components/Header.vue'
import Main from "./components/Main.vue"
import { LanguagesEnum, LanguagesSetEnum } from './enums/LanguagesEnum';
import { ComputedRef, Ref, computed, nextTick, onMounted, ref } from 'vue';
import { SideBarEnum } from './enums/SideBarEnum';
import { CurrentLearnSession } from './interfaces/LearnInterfaces';
import { StatusEnum } from './enums/StatusEnum';
import { ModulesEnum } from './enums/ModulesEnum';
import { Level, LevelsInterface } from './interfaces/LevelsInterfaces';
import { LanguagesConfig } from './interfaces/LanguagesInterfaces';

const langSet: Ref<LanguagesSetEnum> = ref(LanguagesSetEnum.POLEN);
const currentTab: Ref<SideBarEnum | undefined> = ref();
const currenTabComp: ComputedRef<SideBarEnum | undefined> = computed(
  () => currentTab.value
);

const isHeaderShow: Ref<boolean> = ref(true);

const setLangSet = (newlangSet: LanguagesSetEnum,newLangConfig:LanguagesConfig): void => {
localStorage.setItem("configLang", JSON.stringify(newLangConfig));
isHeaderShow.value=false;
  langSet.value = newlangSet;
  nextTick(() => (isHeaderShow.value = true));  
};

const setActiveTab= (tab:SideBarEnum):void=>{
currentTab.value=tab;
}


const levelCompleted = (session:CurrentLearnSession)=>{
    let newLearnSession:CurrentLearnSession | undefined;
    if(session.step===4){
        switch(session.moduleId){
            case ModulesEnum.EASY:
                newLearnSession={
                    moduleId:ModulesEnum.MEDIUM,
                    moduleName: 'Medium Phrases',
                    step:1,
                    status:StatusEnum.IN_PROGRESS,
                    texts: []
                }
                break;
            case ModulesEnum.MEDIUM:
                newLearnSession={
                    moduleId:ModulesEnum.HARD,
                    moduleName: 'Hard Phrases',
                    step:1,
                    status:StatusEnum.IN_PROGRESS,
                    texts: []
                }
                break;
            case ModulesEnum.HARD:
                newLearnSession={
                    moduleId:ModulesEnum.EXTREME,
                    moduleName: 'Extreme Phrases',
                    step:1,
                    status:StatusEnum.IN_PROGRESS,
                    texts: []
                }
                break;
            case ModulesEnum.EXTREME:
            newLearnSession={
                    moduleId:ModulesEnum.EXTREME,
                    moduleName: 'Extreme Phrases',
                    step:4,
                    status:StatusEnum.COMPLETED,
                    texts: []
                }
        }
    }else{
        const helpSession:CurrentLearnSession =session;
        helpSession.step = session.step+1;
        helpSession.texts=[];
        newLearnSession=helpSession;
    }
    localStorage.setItem('currentLearnSession', JSON.stringify(newLearnSession));
    let levelsStatusToInterface:Level[];
    switch(newLearnSession.step){
        case(1):
            levelsStatusToInterface=[
                {step:1 ,status:StatusEnum.IN_PROGRESS},
                {step:2 ,status:StatusEnum.NOT_COMPLETED},
                {step:3 ,status:StatusEnum.NOT_COMPLETED},
                {step:4 ,status:StatusEnum.NOT_COMPLETED},
            ]
            break;
        case(2):
            levelsStatusToInterface=[
                {step:1 ,status:StatusEnum.COMPLETED},
                {step:2 ,status:StatusEnum.IN_PROGRESS},
                {step:3 ,status:StatusEnum.NOT_COMPLETED},
                {step:4 ,status:StatusEnum.NOT_COMPLETED},
            ]
            break;
        case(3):
            levelsStatusToInterface=[
                {step:1 ,status:StatusEnum.COMPLETED},
                {step:2 ,status:StatusEnum.COMPLETED},
                {step:3 ,status:StatusEnum.IN_PROGRESS},
                {step:4 ,status:StatusEnum.NOT_COMPLETED},
            ]
            break;
        case(4):    
            levelsStatusToInterface=[
                {step:1 ,status:StatusEnum.COMPLETED},
                {step:2 ,status:StatusEnum.COMPLETED},
                {step:3 ,status:StatusEnum.COMPLETED},
                {step:4 ,status:StatusEnum.IN_PROGRESS},
            ]
            break;
        default:
            levelsStatusToInterface=[
                {step:1 ,status:StatusEnum.COMPLETED},
                {step:2 ,status:StatusEnum.COMPLETED},
                {step:3 ,status:StatusEnum.COMPLETED},
                {step:4 ,status:StatusEnum.COMPLETED},
            ]
    }
    const newLevelsInterface:LevelsInterface = {
        moduleName: newLearnSession.moduleName,
        moduleId: newLearnSession.moduleId,
        levels:levelsStatusToInterface,
        isCompleted:false


    }
    localStorage.setItem('levelsInterface', JSON.stringify(newLevelsInterface));
    isMainShow.value=false;
    nextTick(()=>isMainShow.value=true)
    currentTab.value=SideBarEnum.LEVELS;

}

const isMainShow:Ref<boolean> = ref(true);


onMounted(() => {
  const langSetFromLocalStorage = localStorage.getItem("langSet");
  if (!langSetFromLocalStorage){
    localStorage.setItem("langSet", LanguagesSetEnum.POLEN);
  }
  if(!localStorage.getItem('configLang')){
    const newLangConfig:LanguagesConfig={
        baseLang:LanguagesEnum.POLISH,
        secondLang:LanguagesEnum.ENGLISH,
    }
    localStorage.setItem('configLang', JSON.stringify(newLangConfig));
  }
  if(!localStorage.getItem('currentLearnSession' || localStorage.getItem('levelsInterface'))){
   currentTab.value=SideBarEnum.SETTINGS;
  }else{
    currentTab.value=SideBarEnum.LEVELS;
  }
  langSet.value = langSetFromLocalStorage as LanguagesSetEnum;
});
</script>
