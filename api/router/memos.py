from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

from api.database import get_db
from api.model import Memos
from api.schemes import MemoRequest

router = APIRouter(prefix="/memos", tags=["memos"])


db_dependency = Annotated[Session, Depends(get_db)]


# API !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~! Routers:
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_memos(db: db_dependency):
    return db.query(Memos).all()


@router.get("/{memo_id}", status_code=status.HTTP_200_OK)
async def read_memo(db: db_dependency, memo_id: int = Path(gt=0)):
    memo_model = db.query(Memos).filter(Memos.id == memo_id).first()
    if memo_model is not None:
        return memo_model
    raise HTTPException(status_code=404, detail="Memo not found!")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_memo(db: db_dependency, memo_req: MemoRequest):
    memo_model = Memos(**memo_req.model_dump())
    db.add(memo_model)
    db.commit()
    return memo_model


@router.put("/{memo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_memo(
    db: db_dependency, memo_req: MemoRequest, memo_id: int = Path(gt=0)
):
    memo_model = db.query(Memos).filter(Memos.id == memo_id).first()
    if memo_model is None:
        raise HTTPException(status_code=404, detail="Memo not found!")
    memo_model.title = memo_req.title
    memo_model.content = memo_req.content

    db.add(memo_model)
    db.commit()


@router.delete("/{memo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_memo(db: db_dependency, memo_id: int = Path(gt=0)):
    memo_model = db.query(Memos).filter(Memos.id == memo_id).first()
    if memo_model is None:
        raise HTTPException(status_code=404, detail="Memo not found!")
    db.query(Memos).filter(Memos.id == memo_id).delete()

    db.commit()
