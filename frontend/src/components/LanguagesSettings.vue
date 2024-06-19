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
import { LanguagesSetEnum } from '../enums/LanguagesEnum';

const emits = defineEmits(["set-lang-set"]);
const chooseLangSet:Ref<LanguagesSetEnum | undefined>=ref();


const setLangSet = (langSet:LanguagesSetEnum):void=>{
    chooseLangSet.value=langSet;
    localStorage.setItem("langSet",langSet);
    emits("set-lang-set",langSet);
}

onMounted(()=>{
    const langSet = localStorage.getItem("langSet");
    if(langSet){
        chooseLangSet.value=langSet as LanguagesSetEnum;
    }
})






</script>