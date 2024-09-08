from pydantic import BaseModel, Field


class BookmarkBase(BaseModel):
    title: str = ""
    description: str = ""
    url: str

    class Config:
        from_attributes = True


class BookmarkResponse(BookmarkBase):
    id: int


class WebUrl(BaseModel):
    url: str

    class Config:
        from_attributes = True


class BookmarkCreate(BookmarkBase):
    pass


class Config(BaseModel):
    sqlite_file_name: str = Field(default="database.db")
    check_same_thread: bool = Field(default=False)
