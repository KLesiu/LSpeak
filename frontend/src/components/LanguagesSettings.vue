<template>
    <section class="lang-settings">
        <h3>Choose languages</h3>
        <section class="lang-settings__options-container">
            <div class="lang-settings__options-container__option" :class="{'active':chooseLangSet===LanguagesSetEnum.POLEN}" @click="setLangSet(LanguagesSetEnum.POLEN)">
                <span>POL/ENG</span>
                <div>
                    <img src="./../assets/polEng.svg" />
                    <img src="./../assets/engPol.svg" />
                </div>
            
            </div>
            <div class="lang-settings__options-container__option" :class="{'active':chooseLangSet===LanguagesSetEnum.POLGER}" @click="setLangSet(LanguagesSetEnum.POLGER)" >
                <span>POL/GER</span>
                <div>
                    <img src="./../assets/polGer.svg" />
                    <img src="./../assets/gerPol.svg" />
                </div>
                
            </div>
        </section>
    </section>
</template>

<script lang="ts" setup>
import { Ref, onMounted, ref } from 'vue';
import { LanguagesEnum, LanguagesSetEnum } from '../enums/LanguagesEnum';
import { LanguagesConfig } from '../interfaces/LanguagesInterfaces';

const emits = defineEmits(["set-lang-set"]);
const chooseLangSet:Ref<LanguagesSetEnum | undefined>=ref();


const setLangSet = (langSet:LanguagesSetEnum):void=>{
    chooseLangSet.value=langSet;
    localStorage.setItem("langSet",langSet);
    const newLangConfigArray = langSet.split("-");
    const newLangConfig:LanguagesConfig = {
        baseLang:newLangConfigArray[0] as LanguagesEnum,
        secondLang:newLangConfigArray[1] as LanguagesEnum

    }
    emits("set-lang-set",langSet,newLangConfig);
}

onMounted(()=>{
    const langSet = localStorage.getItem("langSet");
    if(langSet){
        chooseLangSet.value=langSet as LanguagesSetEnum;
    }
})






</script>