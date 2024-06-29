from fastapi import APIRouter,status
from services.services import transcribe_to_text,compare_text,load_data_by_level
from dependencies import CompareTextRequest,TranscribeTextRequest,LoadDataByLvlRequest
router = APIRouter()

@router.post("/transcribeText",status_code=status.HTTP_200_OK)
def transcribe_text_route(request:TranscribeTextRequest):
    return transcribe_to_text(request.file)

@router.post("/compareText",status_code=status.HTTP_200_OK)
def compare_text_route(request:CompareTextRequest):
    return compare_text(request.textBase,request.text)

@router.post("/getDataByLevel",status_code=status.HTTP_200_OK)
def load_data_by_lvl_route(request:LoadDataByLvlRequest):
    return load_data_by_level(request.level)