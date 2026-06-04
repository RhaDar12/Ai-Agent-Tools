import json
import sys

from asset_pipeline import (
    generate_asset_pipeline,
    img2img_asset_pipeline
)


def to_bool(value):
    if isinstance(value, bool):
        return value

    if value is None:
        return False

    return str(value).strip().lower() in ["1", "true", "yes", "y", "iya", "ya"]


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_asset_pipeline.py <txt2asset|img2asset> ...'
            )

        action = sys.argv[1]

        if action == "txt2asset":
            if len(sys.argv) < 3:
                raise ValueError(
                    'Format: py cli_asset_pipeline.py txt2asset "<prompt>" [negative_prompt] [target] [caption] [do_upscale] [do_remove_bg] [send_to_whatsapp]'
                )

            prompt = sys.argv[2]
            negative_prompt = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "blurry, low quality, distorted, watermark, text, bad anatomy"
            target = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
            caption = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else "Asset dari AI-Agent"
            do_upscale = to_bool(sys.argv[6]) if len(sys.argv) > 6 else False
            do_remove_bg = to_bool(sys.argv[7]) if len(sys.argv) > 7 else False
            send_to_whatsapp = to_bool(sys.argv[8]) if len(sys.argv) > 8 else False

            result = generate_asset_pipeline(
                prompt=prompt,
                negative_prompt=negative_prompt,
                target=target,
                caption=caption,
                do_upscale=do_upscale,
                do_remove_bg=do_remove_bg,
                send_to_whatsapp=send_to_whatsapp
            )

        elif action == "img2asset":
            if len(sys.argv) < 4:
                raise ValueError(
                    'Format: py cli_asset_pipeline.py img2asset "<image_path>" "<prompt>" [negative_prompt] [target] [caption] [denoise] [do_upscale] [do_remove_bg] [send_to_whatsapp]'
                )

            image_path = sys.argv[2]
            prompt = sys.argv[3]
            negative_prompt = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else "blurry, low quality, distorted, watermark, text, bad anatomy"
            target = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
            caption = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] else "Asset img2img dari AI-Agent"
            denoise = float(sys.argv[7]) if len(sys.argv) > 7 and sys.argv[7] else 0.6
            do_upscale = to_bool(sys.argv[8]) if len(sys.argv) > 8 else False
            do_remove_bg = to_bool(sys.argv[9]) if len(sys.argv) > 9 else False
            send_to_whatsapp = to_bool(sys.argv[10]) if len(sys.argv) > 10 else False

            result = img2img_asset_pipeline(
                image_path=image_path,
                prompt=prompt,
                negative_prompt=negative_prompt,
                target=target,
                caption=caption,
                denoise=denoise,
                do_upscale=do_upscale,
                do_remove_bg=do_remove_bg,
                send_to_whatsapp=send_to_whatsapp
            )

        else:
            raise ValueError(f"Action tidak dikenal: {action}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_asset_pipeline",
            "message": "Gagal menjalankan CLI asset pipeline",
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