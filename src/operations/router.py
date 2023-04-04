from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate, OperationGet
from fastapi.exceptions import HTTPException
import time
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/", response_model=list[OperationGet])
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "detail": None
        })

@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        "status": "success",
        "data": None,
        "detail": None
        }

@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    """
    Если бы в функцию передавались какие-то аргументы, то кэш пересчитывался, для каждого изменения этих аргументов
    """
    time.sleep(10)
    return "Много много данных, которые вычислялись сто лет"