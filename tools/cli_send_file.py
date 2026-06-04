import json
import sys

from send_file_whatsapp import send_file_whatsapp


def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError(
                "Format: py cli_send_file.py <file_path> <target> [caption] [delivery_id]"
            )

        file_path = sys.argv[1]
        target = sys.argv[2]
        caption = sys.argv[3] if len(sys.argv) > 3 else ""
        delivery_id = sys.argv[4] if len(sys.argv) > 4 else None

        result = send_file_whatsapp(
            file_path=file_path,
            target=target,
            caption=caption,
            delivery_id=delivery_id
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_send_file",
            "message": "Gagal menjalankan CLI send file",
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