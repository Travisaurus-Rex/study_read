from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tts_job import TTSJob

async def get_all_tts_jobs(db: AsyncSession):
    result = await db.execute(select(TTSJob).order_by(TTSJob.created_at.desc()))
    return result.scalars().all()

async def create_tts_job(db: AsyncSession, text: str, voice_id: str | None, provider: str | None):
    job = TTSJob(
        text = text,
        voice_id = voice_id,
        provider = provider
    )
    
    db.add(job)
    await db.commit()
    await db.refresh(job)
    return job