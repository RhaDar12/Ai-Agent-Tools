import json
import sys

from stt_tool import transcribe_audio


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_stt.py "<audio_file_path>" [model_size] [language]'
            )

        file_path = sys.argv[1]
        model_size = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else "base"
        language = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "id"

        result = transcribe_audio(
            file_path=file_path,
            model_size=model_size,
            language=language
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_stt",
            "message": "Gagal menjalankan CLI STT",
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