<template>
    <section class="learn">
      <div class="learn__header">
        <div>
          <h2>Module: {{ currentLearnSession.moduleName }}</h2>
          <span>Step: {{ currentLearnSession.step }}</span>
        </div>
        <div class="learn__header__timer">
          <span :class="{ 'expiring': timer < 10 }">{{ timer }}s</span>
          <Hourglass />
        </div>
      </div>
      <div class="learn__main">
        <div class="learn__main__baseLang">
          <img :src="returnBaseLangImage()" />
          <span>Jak sie masz?</span>
        </div>
        <div class="learn__main__microphoneContainer">
          <img
            class="learn__main__microphoneContainer__micro"
            @click="toggleMicro"
            :src="returnMicroImage"
          />
          <img
            class="learn__main__microphoneContainer__lang"
            :src="returnSecondLangImage()"
          />
          <audio ref="audioPlayer" controls></audio>
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
  import { PropType, Ref, computed, onUnmounted, ref } from 'vue';
  import { CurrentLearnSession } from './../interfaces/LearnInterfaces';
  import Hourglass from './Hourglass.vue';
  
  const props = defineProps({
    currentLearnSession: { type: Object as PropType<CurrentLearnSession>, required: true }
  });
  
  const isMicrophoneActive: Ref<boolean> = ref(false);
  
  const configLang = JSON.parse(localStorage.getItem('configLang')!);
  const timer: Ref<number> = ref(90);
  
  const returnBaseLangImage = () => `/src/assets/${configLang.baseLang}.svg`;
  const returnSecondLangImage = () => `/src/assets/${configLang.secondLang}.svg`;
  const returnMicroImage = computed(() => (isMicrophoneActive.value ? '/src/assets/micro-active.svg' : '/src/assets/micro.svg'));
  
  const toggleMicro = (): void => {
    isMicrophoneActive.value = !isMicrophoneActive.value;
    if (isMicrophoneActive.value) startRecording();
    else{
        stopRecording();
        mediaRecorder.value!.stream.getTracks().forEach((track) => track.stop());

    } 
  };
  
  setInterval(() => {
    timer.value--;
  }, 1000);
  
  const audioPlayer = ref<HTMLAudioElement | null>(null);
  const mediaRecorder: Ref<MediaRecorder | null> = ref(null);
  const audioChunks: Ref<BlobPart[]> = ref([]);
  
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder.value = new MediaRecorder(stream);
  
      mediaRecorder.value.ondataavailable = (event) => {
        audioChunks.value.push(event.data);
      };
  
      mediaRecorder.value.onstop = () => {
        const audioBlob = new Blob(audioChunks.value, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        if (audioPlayer.value) {
          audioPlayer.value.src = audioUrl;
        }
  
        // Convert the Blob to bytes
        const reader = new FileReader();
        reader.onloadend = async() => {
            const base64result = arrayBufferToBase64(reader.result as ArrayBuffer)
            await sendToTranslate(base64result)
        };
        reader.readAsArrayBuffer(audioBlob);
  
        audioChunks.value = [];
      };
  
      mediaRecorder.value.start();
    } catch (error) {
      console.error('Error accessing microphone:', error);
    }
  };
  
  const arrayBufferToBase64 = (arrayBuffer: ArrayBuffer): string => {
  const uint8Array = new Uint8Array(arrayBuffer);
  const binaryString = Array.prototype.map.call(uint8Array, (byte: number) => {
    return String.fromCharCode(byte);
  }).join('');

  return btoa(binaryString);
};
  const stopRecording = () => {
    if (mediaRecorder.value) {
      mediaRecorder.value.stop();
    }
  };
  
  const sendToTranslate = async(bytes:string) => {
    const result = await fetch('http://localhost:8000/transcribeText',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            file:bytes
        })
    })
    console.log(result)
  };
 
  
  onUnmounted(() => {
    if (mediaRecorder.value) {
      mediaRecorder.value.stream.getTracks().forEach((track) => track.stop());
    }
  });
  </script>
  
  <style scoped>
  button {
    margin-right: 10px;
  }
  </style>
  