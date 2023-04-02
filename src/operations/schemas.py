from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    type: str


class OperationGet(OperationCreate):
    class Config:
        orm_mode = True
