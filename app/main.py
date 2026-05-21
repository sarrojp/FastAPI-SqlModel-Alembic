from fastapi import Depends, FastAPI, HTTPException

from sqlmodel import select
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session, init_db
from app.models import Song, SongCreate


#@asynccontextmanager
#async def lifespan(app: FastAPI):
 #   await init_db()
  #  yield

app = FastAPI(lifespan=lifespan)


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song



@app.put("/songs/{song_id}", response_model=Song)
async def update_song(
    song_id: int,
    updated_song: SongCreate,
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(
        select(Song).where(Song.id == song_id)
    )

    song = result.scalar_one_or_none()

    if not song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )

    song.name = updated_song.name
    song.artist = updated_song.artist

    session.add(song)

    await session.commit()
    await session.refresh(song)

    return song


@app.delete("/songs/{song_id}")
async def delete_song(
    song_id: int,
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(
        select(Song).where(Song.id == song_id)
    )

    song = result.scalar_one_or_none()

    if not song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )

    await session.delete(song)

    await session.commit()

    return {
        "message": f"Song with id {song_id} deleted successfully"
    }