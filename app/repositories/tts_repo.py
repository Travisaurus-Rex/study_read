from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tts_job import TTSJob

async def get_all_tts_jobs(db: AsyncSession):
    result = await db.execute(select(TTSJob).order_by(TTSJob.created_at.desc()))
    return result.scalars().all()