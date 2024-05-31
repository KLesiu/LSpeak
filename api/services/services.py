import assemblyai as aai
import os
from dotenv import load_dotenv
load_dotenv()
aai.settings.api_key = os.getenv('ASSEMBLYAI_KEY')


def transcribe_to_text(file:str):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file)
    return transcript.text

