
import assemblyai as aai
import os
from fuzzywuzzy import process
from fastapi import  HTTPException
from helpers.dbHelper import load_data
from dotenv import load_dotenv
from helpers.convertMachineHelper import base64_to_binary_io
load_dotenv()
aai.settings.api_key = os.getenv('ASSEMBLYAI_KEY')


def transcribe_to_text(file:str)->str:
    transcriber = aai.Transcriber()
    audio_binary_io = base64_to_binary_io(file)
    transcript = transcriber.transcribe(audio_binary_io)
    return transcript.text

def compare_text(textBase:str,text:str)-> list:
    textBase_words = textBase.split()
    text_words = text.split()
    mistakes = []
    for word in text_words:
        best_match = process.extractOne(word,textBase_words)
        if(best_match[1] < 95):
            mistakes.append(word)
    return mistakes

def load_data_by_level(level:str)->list:
    data = load_data()
    if(level in data):
        return data[level]
    return  HTTPException(status_code=404,detail='Level not found')
 

