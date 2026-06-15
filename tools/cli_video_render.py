"""
cli_video_render.py - CLI untuk AI-Agent Tool: Render ASCII Terminal Video

Format:
    py cli_video_render.py [duration] [target] [caption]
    
Contoh:
    py cli_video_render.py 8 "166095042437336@lid" "Terminal video from AI-Agent Tools"
"""

import json
import sys
from pathlib import Path

# Tambahin current dir ke path biar bisa import video_render
sys.path.insert(0, str(Path(__file__).parent))

from video_render import render_video


def main():
    try:
        duration = float(sys.argv[1]) if len(sys.argv) > 1 else 8
        target = sys.argv[2] if len(sys.argv) > 2 else None
        caption = sys.argv[3] if len(sys.argv) > 3 else "Terminal ASCII Video dari AI-Agent Tools"

        result = render_video(
            duration=duration,
            target=target,
            caption=caption
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_video_render",
            "message": "Gagal menjalankan CLI video render",
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
