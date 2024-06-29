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
                <input v-model="soundValue" @change="changeSoundValue" type="range" min="0" max="100" step="1" ref="inputRange">
            </div>
        </section>
    </section>
</template>

<script lang="ts" setup>
import { Ref, nextTick, onMounted, ref } from 'vue';


const soundValue:Ref<number> = ref(50);
const isSoundEffectOn:Ref<boolean> = ref(true);
const inputRange = ref<HTMLInputElement | null>(null);


const changeSoundValue = (event: Event):void => {
    const target = event.target as HTMLInputElement;
    localStorage.setItem('soundValue', target.value);
}
const changeSoundEffect = (value:boolean):void => {
    isSoundEffectOn.value = value
    localStorage.setItem('isSoundEffectOn', value.toString());
}



const setBackgroundSize = (input: HTMLInputElement): void => {
    if(!input) return;
    input.style.setProperty("--background-size", `${getBackgroundSize(input)}%`);
    
}

const getBackgroundSize = (input: HTMLInputElement): number => {
    const min = +input.min || 0;
    const max = +input.max || 100;
    const value = +input.value;
    const size = ((value - min) / (max - min)) * 100;
    return size;
}

onMounted(async() => {
    const soundValueFromLocalStorage = localStorage.getItem('soundValue');
    const isSoundEffectOnFromLocalStorage = localStorage.getItem('isSoundEffectOn');
    if(soundValueFromLocalStorage) soundValue.value = parseInt(soundValueFromLocalStorage);
    if(isSoundEffectOnFromLocalStorage) isSoundEffectOn.value = isSoundEffectOnFromLocalStorage === 'true';
    await nextTick();
    
    if (inputRange.value) {
        setBackgroundSize(inputRange.value);
        inputRange.value.addEventListener("input", () => setBackgroundSize(inputRange.value!));
    }
})
</script>