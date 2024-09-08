from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from ..schema.bookmark import WebUrl, BookmarkResponse
from ..dependency import get_db
from ..utils import crud
from ..utils.link_meta import get_meta


router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=BookmarkResponse)
async def create_bookmark(url: WebUrl, db: Session = Depends(get_db)):
    url_metadata = get_meta(url.url)
    return crud.create_bookmark(db, url_metadata)


@router.get("/", response_model=List[BookmarkResponse])
async def get_all_bookmarks(db: Session = Depends(get_db)):
    return crud.get_bookmarks(db)


@router.get("/{url_id}", response_model=BookmarkResponse)
async def get_bookmark(url_id: str, db: Session = Depends(get_db)):
    bookmark = crud.get_bookmark(db, url_id)

    if not bookmark:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No link with id '{url_id}' found.",
        )
    return bookmark


@router.delete("/{url_id}")
async def delete_bookmark(url_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_bookmark(db, url_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cannot delete link with '{url_id}'.",
        )
    return {"success": f"Bookmark with '{url_id}' deleted."}
