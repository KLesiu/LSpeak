
from typing import Dict, List
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
    """
    Transcribes the given audio file to text.

    Args:
        file (str): The path to the audio file.

    Returns:
        str: The transcribed text.

    """
    transcriber = aai.Transcriber()
    audio_binary_io = base64_to_binary_io(file)
    transcript = transcriber.transcribe(audio_binary_io)
    return transcript.text

def compare_text(textBase: str, text: str) -> list:
    """
    Compares two texts and returns a list of words that have a similarity score below 95%.

    Args:
        textBase (str): The base text to compare against.
        text (str): The text to compare.

    Returns:
        list: A list of words that have a similarity score below 95%.
    """
    textBase_words = textBase.split()
    text_words = text.split()
    mistakes = []
    for word in text_words:
        best_match = process.extractOne(word, textBase_words)
        if best_match[1] < 95:
            mistakes.append(word)
    return mistakes

def load_data_by_level(level: str) -> list:
    """
    Load data by level.

    Args:
        level (str): The level of data to load.

    Returns:
        list: The data corresponding to the specified level.

    Raises:
        HTTPException: If the specified level is not found in the data.
    """
    data = load_data()
    if level in data:
        return data[level]
    return HTTPException(status_code=404, detail='Level not found')

 
def load_all_data() -> Dict[str, List[Dict[str, str]]]:
    """
    Loads all data.

    Returns:
        A dictionary containing multiple lists of dictionaries, where each dictionary represents a data entry.
    """
    data = load_data()
    return data


