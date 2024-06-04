import assemblyai as aai
import os
from io import BytesIO
from fuzzywuzzy import process
from fastapi import  HTTPException
from helpers.dbHelper import load_data
from dotenv import load_dotenv
load_dotenv()
aai.settings.api_key = os.getenv('ASSEMBLYAI_KEY')


def transcribe_to_text(file:bytes)->str:
    transcriber = aai.Transcriber()
    audio_data = BytesIO(file)
    transcript = transcriber.transcribe(audio_data)
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
    return HTTPException(status_code=404,detail='Level not found')
 


