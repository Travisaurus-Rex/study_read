from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from app.db.base import Base

class TTSJob(Base):
    __tablename__ = "tts_jobs"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    voice_id = Column(String, nullable=True)
    provider = Column(String, nullable=True)
    audio_path = Column(String, nullable=True)
    duration_seconds = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())