import json
import sys

from tts_tool import generate_tts


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_tts.py "<text>" [voice] [rate] [target] [caption]'
            )

        text = sys.argv[1]
        voice = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else "id-ID-ArdiNeural"
        rate = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "+0%"
        target = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
        caption = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else "Audio TTS dari AI-Agent"

        result = generate_tts(
            text=text,
            voice=voice,
            rate=rate,
            target=target,
            caption=caption
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_tts",
            "message": "Gagal menjalankan CLI TTS",
            "file_path": None,
            "delivered_file": {
                "status": "failed",
                "sent_to": None,
                "sent_at": None,
                "delivery_id": None
            },
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()