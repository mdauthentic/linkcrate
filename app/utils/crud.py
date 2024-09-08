from sqlalchemy.orm import Session
from app.schema.bookmark import BookmarkCreate
from ..models.bookmark import Bookmark


def get_bookmark(db: Session, url_id: int):
    return db.query(Bookmark).filter(Bookmark.id == url_id).first()


def get_bookmarks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Bookmark).offset(skip).limit(limit).all()


def create_bookmark(db: Session, bookmark: BookmarkCreate) -> Bookmark:
    db_link = Bookmark(
        title=bookmark.title, description=bookmark.description, url=bookmark.url
    )
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


def update_bookmark(db: Session, bookmark_id: int, update_data: dict):
    link = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
    if link:
        for key, value in update_data.items():
            setattr(link, key, value)
        db.commit()
        db.refresh(link)
        return link
    return None


def delete_bookmark(db: Session, bookmark_id: int):
    link = db.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
    if link:
        db.delete(link)
        db.commit()
        return True
    return False
