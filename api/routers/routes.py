from fastapi import APIRouter, status
from services.services import transcribe_to_text, compare_text, load_data_by_level
from dependencies import CompareTextRequest, TranscribeTextRequest, LoadDataByLvlRequest

router = APIRouter()

@router.post("/transcribeText", status_code=status.HTTP_200_OK)
def transcribe_text(request: TranscribeTextRequest):
    # """
    # Transcribes the given text file to text.
    # """
    return transcribe_to_text(request.file)

@router.post("/compareText", status_code=status.HTTP_200_OK)
def compare_text(request: CompareTextRequest):
    # """
    # Compares two texts and returns the comparison result.
    # """
    return compare_text(request.textBase, request.text)

@router.post("/getDataByLevel", status_code=status.HTTP_200_OK)
def load_data_by_lvl(request: LoadDataByLvlRequest):
    # """
    # Loads data based on the given level.
    # """
    return load_data_by_level(request.level)
