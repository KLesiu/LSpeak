from pydantic import BaseModel
class CompareTextRequest(BaseModel):
    textBase:str
    text:str

class TranscribeTextRequest(BaseModel):
    file:str

class LoadDataByLvlRequest(BaseModel):
    level:str
