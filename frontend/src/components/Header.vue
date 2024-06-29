<template>
  <header>
    <h1><span class="firstLetter">L</span>Speak</h1>
    <section>
      <div class="languages" v-if="props.langSet === LanguagesSetEnum.POLEN">
        <img
          @click="changeOpacity(LanguagesEnum.POLISH)"
          src="./../assets//polEng.svg"
          :class="{ active: config.baseLang === LanguagesEnum.POLISH }"
        />
        <img
          @click="changeOpacity(LanguagesEnum.ENGLISH)"
          src="./../assets/engPol.svg"
          :class="{ active: config.baseLang === LanguagesEnum.ENGLISH }"
        />
      </div>
      <div class="languages" v-else>
        <img
          @click="changeOpacity(LanguagesEnum.POLISH)"
          src="./../assets/polGer.svg"
          :class="{ active: config.baseLang === LanguagesEnum.POLISH }"
        />
        <img
          @click="changeOpacity(LanguagesEnum.GERMANY)"
          src="./../assets/gerPol.svg"
          :class="{ active: config.baseLang === LanguagesEnum.GERMANY }"
        />
      </div>
    </section>
  </header>
</template>

<script setup lang="ts">
import { LanguagesEnum, LanguagesSetEnum } from "./../enums/LanguagesEnum";
import { LanguagesConfig } from "../interfaces/LanguagesInterfaces";
import { PropType, Ref, onMounted, ref } from "vue";

const props = defineProps({
  langSet: {
    type: String as PropType<LanguagesSetEnum>,
    default: LanguagesSetEnum.POLEN,
  },
});

const config: Ref<LanguagesConfig> = ref({
  baseLang: LanguagesEnum.POLISH,
  secondLang: LanguagesEnum.ENGLISH,
});

const changeOpacity = (baseLang: LanguagesEnum): void => {
  config.value.secondLang = config.value.baseLang;
  config.value.baseLang = baseLang;
  localStorage.setItem("configLang", JSON.stringify(config.value));
};
onMounted(() => {
  const configFromLocalStorage = JSON.parse(
    `${localStorage.getItem("configLang")}`
  );
  if (!configFromLocalStorage) {
    if (localStorage.getItem("langSet")) {
      switch (localStorage.getItem("langSet")) {
        case LanguagesSetEnum.POLEN:
          config.value.baseLang = LanguagesEnum.POLISH;
          config.value.secondLang = LanguagesEnum.ENGLISH;
          break;
        case LanguagesSetEnum.POLGER:
          config.value.baseLang = LanguagesEnum.POLISH;
          config.value.secondLang = LanguagesEnum.GERMANY;
          break;
      }
      return;
    }
  }
  config.value = configFromLocalStorage;
});
</script>
