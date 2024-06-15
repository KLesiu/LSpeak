

<template>
    <header>
    
            <h1>
                <span class="firstLetter">L</span>Speak
            </h1>
            <Languages :config="config" />
           
        
    </header>
</template>


<script setup lang="ts">
import Languages from "./Languages.vue"
import {LanguagesEnum} from "./../enums/LanguagesEnum"
import { LanguagesConfig } from "../interfaces/LanguagesInterfaces";


const config:LanguagesConfig = {
    baseLang: LanguagesEnum.POLISH,
    secondLang: LanguagesEnum.ENGLISH
}

</script>

