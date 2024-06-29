<template>
    <section class="learn">
      <div class="learn__header">
        <div>
          <h2>Module: {{ currentLearnSession.moduleName }}</h2>
          <span>Step: {{currentLearnSession.step}}</span>
        </div>
        <div class="learn__header__timer">
          <span :class="{ 'expiring': timer < 10 }">{{ timer }}s</span>
          <Hourglass />
        </div>
      </div>
      <div class="learn__main">
        <div class="learn__main__baseLang">
          <img :src="returnBaseLangImage()" />
          <span>{{ wordToTranslateComp }}</span>
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
          <audio class="" ref="audioPlayer" controls></audio>
        </div>
        <div class="learn__main__resultContainer">
          <div class="learn__main__resultContainer__result">
            <img :src="returnSecondLangImage()" />
            <input type="text" v-model="test">
            <span v-if="userWordTranslatedComp" class="learn__main__resultContainer__result__userWord" :class="{'incorrect':wordMistakes?.length}">{{ userWordTranslatedComp}}</span>
            <span v-else>.....</span>
          </div>
          <span class="learn__main__resultContainer__correctAnswer" v-if="userWordTranslatedComp">{{ correctWordTranslateComp }}</span>
        </div>
      </div>
    </section>
    <section v-if="wordMistakes?.length" class="mask">
      <button @click="repeatLevel">Play again</button>
      <button @click="exitToLevels">Exit</button>
    </section>
  </template>
  
  <script lang="ts" setup>
  import { PropType, Ref, computed,  onMounted,  onUnmounted, ref } from 'vue';
  import { CurrentLearnSession, Question } from './../interfaces/LearnInterfaces';
  import Hourglass from './Hourglass.vue';
  

const test:Ref<string> = ref('')

  const props = defineProps({
    currentLearnSession: { type: Object as PropType<CurrentLearnSession>, required: true }
  });

  const emits = defineEmits(['exitToLevels','levelCompleted'])
  
  const isMicrophoneActive: Ref<boolean> = ref(false);
  
  const configLang = JSON.parse(localStorage.getItem('configLang')!);
  const timer: Ref<number> = ref(30);
  
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
    if(timer.value === 0) return
    timer.value--;
    if(timer.value === 0) wordMistakes.value = ['Time is over']
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
  const resetTimer = () => {
    timer.value = 30;
  };
  
  const sendToTranslate = async(bytes:string) => {
    // const result = await fetch('http://localhost:8000/transcribeText',{
    //     method:'POST',
    //     headers:{
    //         'Content-Type': 'application/json'
    //     },
    //     body:JSON.stringify({
    //         file:bytes
    //     })
    // }).then(res=>res.json()).catch(err=>console.error(err))
    
    userWordTranslated.value =test.value
    compareWords()
  };

  const compareWords = async()=>{
    const result = await fetch('http://localhost:8000/compareText',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            textBase:correctWordTranslateComp.value,
            text: userWordTranslatedComp.value
        })
    }).then(res=>res.json()).catch(err=>console.error(err))
    if(!result.length) getNextLevel()
    else wordMistakes.value=result
    
  }

  const repeatLevel = ()=>{
    userWordTranslated.value=''
    wordMistakes.value=[]
    resetTimer()
    
  }

  const getNextLevel = ()=>{
    if(!props.currentLearnSession) return
    if(stepOnLevel.value===props.currentLearnSession.texts.length-1){
      return emits("levelCompleted",props.currentLearnSession)
    } 
    stepOnLevel.value++
    setTimeout(()=>{
      userWordTranslated.value=''
      wordToTranslate.value = props.currentLearnSession.texts[stepOnLevel.value][configLang.baseLang as keyof Question]
      correctWordTranslate.value = props.currentLearnSession.texts[stepOnLevel.value][configLang.secondLang as keyof Question]
      resetTimer()
    },1000)
  
  }



  const exitToLevels = ()=>{
    emits("exitToLevels")
  }

  const wordToTranslate = ref()
  const wordToTranslateComp = computed(()=>wordToTranslate.value)

  const userWordTranslated = ref('')
  const userWordTranslatedComp = computed(()=>userWordTranslated.value)

  const correctWordTranslate = ref()
  const correctWordTranslateComp = computed(()=>correctWordTranslate.value)

  const wordMistakes:Ref<string[] | undefined> = ref([])
  const stepOnLevel: Ref<number> = ref(0);
  
onMounted(()=>{
  wordToTranslate.value = props.currentLearnSession.texts[0][configLang.baseLang as keyof Question]
  correctWordTranslate.value = props.currentLearnSession.texts[0][configLang.secondLang as keyof Question]
})

  onUnmounted(() => {
    if (mediaRecorder.value) {
      mediaRecorder.value.stream.getTracks().forEach((track) => track.stop());
    }
  });
  </script>
  

  