<template>
  <section>
    <div  class="languages" v-if="languages.baseLang === LanguagesEnum.ENGLISH || languages.baseLang || LanguagesEnum.POLISH" >
        <img @click="changeOpacity(LanguagesEnum.POLISH)" src="./../assets//polEng.svg" :class="{'active':languages.baseLang===LanguagesEnum.POLISH}"/>
        <img @click="changeOpacity(LanguagesEnum.ENGLISH)" src="./../assets/engPol.svg" :class="{'active':languages.baseLang===LanguagesEnum.ENGLISH}" />
    </div>
    <div  class="languages" v-else>
        <img @click="changeOpacity(LanguagesEnum.POLISH)" src="./../assets/polGer.svg" :class="{'active':languages.baseLang === LanguagesEnum.POLISH }"  />
        <img @click="changeOpacity(LanguagesEnum.GERMANY)" src="./../assets/gerPol.svg" :class="{'active':languages.baseLang === LanguagesEnum.GERMANY}" />
    </div>
   
    
  </section>
</template>

<script lang="ts" setup>
import { PropType, defineProps,Ref, ref } from "vue";
import { LanguagesConfig } from "./../interfaces/LanguagesInterfaces";
import { LanguagesEnum } from "../enums/LanguagesEnum";

const props = defineProps({
  config: {
    type: Object as PropType<LanguagesConfig>,
    required: true,
  },
});
const languages: Ref<LanguagesConfig> = ref(props.config);


const changeOpacity=(baseLang:LanguagesEnum):void=>{
    languages.value.secondLang=languages.value.baseLang;
    languages.value.baseLang=baseLang;
}
</script>
