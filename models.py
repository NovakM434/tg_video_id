from sqlalchemy import Column, String

from settings.database import Base


class Video(Base):
    __tablename__ = 'videos'

    command = Column(String, primary_key=True)
    video_id = Column(String)


class Audio(Base):
    __tablename__ = 'audio'
    command = Column(String, primary_key=True)
    audio_id = Column(String)
