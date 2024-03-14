from pyrogram import Client, filters
from sqlalchemy.future import select
from sqlalchemy import func

from models import Video, Audio
from settings.database import async_session_maker


def register_handlers(app: Client):
    @app.on_message(filters.private & filters.video_note)
    async def video_note_handler(client, message):
        video_note_id = message.video_note.file_id
        await message.reply_text(video_note_id)

        async with async_session_maker() as session:
            circle_count = await session.execute(select(func.count(Video.command)).where(Video.command.like('circle%')))
            circle_count = circle_count.scalar()
            new_video = Video(command=f'circle{circle_count + 1}', video_id=video_note_id)
            session.add(new_video)
            await session.commit()

    @app.on_message(filters.regex(r'^circle\d+$'))
    async def message_circle_handler(client, message):
        search_term = message.text
        async with async_session_maker() as session:
            result = await session.execute(select(Video).where(Video.command == search_term))
            video = result.scalar()

            if video:
                await message.delete()
                await client.send_video_note(
                    chat_id=message.chat.id,
                    video_note=video.video_id
                )

    @app.on_message(filters.private & filters.voice)
    async def audio_note_handler(client, message):
        audio_id = message.voice.file_id
        await message.reply_text(audio_id)

        async with async_session_maker() as session:
            audionote_count = await session.execute(select(func.count(Audio.command)).where(Audio.command.like('audionote%')))
            audionote_count = audionote_count.scalar()
            new_audio = Audio(command=f'audionote{audionote_count + 1}', audio_id=audio_id)
            session.add(new_audio)
            await session.commit()

    @app.on_message(filters.regex(r'^audionote\d+$'))
    async def message_voice_handler(client, message):
        search_term = message.text
        async with async_session_maker() as session:
            result = await session.execute(select(Audio).where(Audio.command == search_term))
            audio = result.scalar()

            if audio:
                await message.delete()
                await client.send_voice(
                    chat_id=message.chat.id,
                    voice=audio.audio_id
                )
