from sqlmodel import SQLModel, Field
from typing import Optional


class SongBase(SQLModel):
    name: str
    artist: str


class Song(SongBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass