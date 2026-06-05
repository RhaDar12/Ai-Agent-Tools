import json
import sys

from bg_remove_tool import remove_background


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_bg_remove.py "<image_path>" [target] [caption]'
            )

        image_path = sys.argv[1]
        target = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else None
        caption = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "Gambar tanpa background dari AI-Agent"

        result = remove_background(
            image_path=image_path,
            target=target,
            caption=caption
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_bg_remove",
            "message": "Gagal menjalankan CLI remove background",
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