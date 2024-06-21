<template>
    <section class="sound-settings">
        <h3>Lessons experience</h3>
        <section class="sound-settings__options-container">
            <div class="sound-settings__options-container__option">
                <span>Sound effects</span>
                <div class="sound-settings__options-container__option__sound-effects">
                    <button @click="changeSoundEffect(true)" :class="{'active':isSoundEffectOn}">on</button>
                    <button @click="changeSoundEffect(false)" :class="{'active':!isSoundEffectOn}">off</button>
                </div>
            </div>
            <div class="sound-settings__options-container__option">
                <span>Volume</span>
                <input v-model="soundValue" @change="changeSoundValue" type="range">
            </div>
        </section>
    </section>
</template>

<script lang="ts" setup>
import { Ref, onMounted, ref } from 'vue';


const soundValue:Ref<number> = ref(50);
const isSoundEffectOn:Ref<boolean> = ref(true);

const changeSoundValue = (event: Event):void => {
    const target = event.target as HTMLInputElement;
    localStorage.setItem('soundValue', target.value);
}
const changeSoundEffect = (value:boolean):void => {
    isSoundEffectOn.value = value
    localStorage.setItem('isSoundEffectOn', value.toString());
}

onMounted(() => {
    const soundValueFromLocalStorage = localStorage.getItem('soundValue');
    const isSoundEffectOnFromLocalStorage = localStorage.getItem('isSoundEffectOn');
    if(soundValueFromLocalStorage) soundValue.value = parseInt(soundValueFromLocalStorage);
    if(isSoundEffectOnFromLocalStorage) isSoundEffectOn.value = isSoundEffectOnFromLocalStorage === 'true';
})
</script>