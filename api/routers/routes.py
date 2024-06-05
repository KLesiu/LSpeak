from fastapi import APIRouter,status
from services.services import transcribe_to_text,compare_text,load_data_by_level
from dependencies import CompareTextRequest,TranscribeTextRequest,LoadDataByLvlRequest
router = APIRouter()

@router.post("/transcribeText",status_code=status.HTTP_200_OK)
async def transcribe_text(request:TranscribeTextRequest):
    return await transcribe_to_text(request.file)

@router.post("/compareText",status_code=status.HTTP_200_OK)
async def compare_text(request:CompareTextRequest):
    return await compare_text(request.textBase,request.text)

@router.post("/getDataByLevel",status_code=status.HTTP_200_OK)
async def load_data_by_lvl(request:LoadDataByLvlRequest):
    return await load_data_by_level(request.level)