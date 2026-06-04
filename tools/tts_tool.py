import asyncio
from pathlib import Path

import edge_tts

from core import (
    DIRS,
    ensure_dirs,
    make_id,
    success_response,
    error_response
)

from delivered_file import create_delivery_record


DEFAULT_VOICE = "id-ID-GadisNeural"


async def _generate_tts_async(text, output_path, voice=DEFAULT_VOICE, rate="+0%"):
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate
    )
    await communicate.save(str(output_path))


def generate_tts(text, voice=DEFAULT_VOICE, rate="+0%", target=None, caption="Audio TTS dari AI-Agent"):
    """
    Generate audio TTS dari teks.
    Output: MP3
    """

    tool_name = "generate_tts"

    try:
        ensure_dirs()

        if not text or not text.strip():
            raise ValueError("Text kosong, tidak bisa membuat TTS.")

        audio_id = make_id("tts")
        output_path = DIRS["audio"] / f"{audio_id}.mp3"

        asyncio.run(
            _generate_tts_async(
                text=text,
                output_path=output_path,
                voice=voice,
                rate=rate
            )
        )

        delivery = create_delivery_record(
            file_path=output_path,
            target=target,
            caption=caption
        )

        return success_response(
            tool=tool_name,
            message="TTS berhasil dibuat",
            file_path=output_path,
            extra={
                "audio_id": audio_id,
                "voice": voice,
                "rate": rate,
                "delivery_id": delivery.get("delivery_id"),
                "delivery_record": delivery.get("delivery_record"),
                "delivered_file": {
                    "status": "pending",
                    "sent_to": target,
                    "sent_at": None,
                    "delivery_id": delivery.get("delivery_id")
                }
            }
        )

    except Exception as e:
        return error_response(tool_name, e)