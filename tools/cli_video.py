import json
import sys

from video_tool import (
    create_video_from_text,
    create_video_from_image,
    create_slideshow_video
)


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_video.py <text|image|slideshow> ...'
            )

        mode = sys.argv[1]

        if mode == "text":
            if len(sys.argv) < 3:
                raise ValueError(
                    'Format: py cli_video.py text "<text>" [duration] [target] [caption]'
                )

            text = sys.argv[2]
            duration = float(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else 8
            target = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
            caption = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else "Video dari teks AI-Agent"

            result = create_video_from_text(
                text=text,
                duration=duration,
                target=target,
                caption=caption
            )

        elif mode == "image":
            if len(sys.argv) < 3:
                raise ValueError(
                    'Format: py cli_video.py image "<image_path>" [duration] [audio_path] [target] [caption]'
                )

            image_path = sys.argv[2]
            duration = float(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else 8
            audio_path = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
            target = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
            caption = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] else "Video dari gambar AI-Agent"

            result = create_video_from_image(
                image_path=image_path,
                duration=duration,
                audio_path=audio_path,
                target=target,
                caption=caption
            )

        elif mode == "slideshow":
            if len(sys.argv) < 3:
                raise ValueError(
                    'Format: py cli_video.py slideshow "<image1|image2|image3>" [seconds_per_image] [audio_path] [target] [caption]'
                )

            image_paths = sys.argv[2]
            seconds_per_image = float(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else 3
            audio_path = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
            target = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
            caption = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] else "Slideshow video AI-Agent"

            result = create_slideshow_video(
                image_paths=image_paths,
                seconds_per_image=seconds_per_image,
                audio_path=audio_path,
                target=target,
                caption=caption
            )

        else:
            raise ValueError(f"Mode tidak dikenal: {mode}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_video",
            "message": "Gagal menjalankan CLI Video",
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