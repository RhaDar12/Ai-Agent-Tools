import json
import sys
from screenshot_pc import take_screenshot, take_screenshot_region


def main():
    try:
        mode = "full"
        target = None
        caption = "Screenshot dari PC"

        if len(sys.argv) > 1:
            mode = sys.argv[1]

        if len(sys.argv) > 2:
            target = sys.argv[2]

        if len(sys.argv) > 3:
            caption = sys.argv[3]

        if mode == "full":
            result = take_screenshot(
                target=target,
                caption=caption
            )

        elif mode == "region":
            if len(sys.argv) < 8:
                raise ValueError(
                    "Mode region butuh argumen: region target caption x y width height"
                )

            x = int(sys.argv[4])
            y = int(sys.argv[5])
            width = int(sys.argv[6])
            height = int(sys.argv[7])

            result = take_screenshot_region(
                x=x,
                y=y,
                width=width,
                height=height,
                target=target,
                caption=caption
            )

        else:
            raise ValueError(f"Mode tidak dikenal: {mode}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_screenshot",
            "message": "Gagal menjalankan CLI screenshot",
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