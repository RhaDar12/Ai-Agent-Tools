import json
import sys

from pc_control_tool import (
    get_mouse_position,
    click_screen,
    move_mouse,
    type_text,
    press_key,
    hotkey,
    scroll,
    wait_seconds,
    open_path,
    open_app,
    run_safe_command
)


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                "Format: py cli_pc.py <action> [args...]"
            )

        action = sys.argv[1]

        if action == "position":
            result = get_mouse_position()

        elif action == "click":
            if len(sys.argv) < 4:
                raise ValueError("Format: py cli_pc.py click <x> <y> [button] [clicks]")

            x = sys.argv[2]
            y = sys.argv[3]
            button = sys.argv[4] if len(sys.argv) > 4 else "left"
            clicks = sys.argv[5] if len(sys.argv) > 5 else 1

            result = click_screen(x, y, button, clicks)

        elif action == "move":
            if len(sys.argv) < 4:
                raise ValueError("Format: py cli_pc.py move <x> <y> [duration]")

            x = sys.argv[2]
            y = sys.argv[3]
            duration = sys.argv[4] if len(sys.argv) > 4 else 0.2

            result = move_mouse(x, y, duration)

        elif action == "type":
            if len(sys.argv) < 3:
                raise ValueError('Format: py cli_pc.py type "<text>"')

            text = sys.argv[2]
            result = type_text(text)

        elif action == "press":
            if len(sys.argv) < 3:
                raise ValueError("Format: py cli_pc.py press <key>")

            key = sys.argv[2]
            result = press_key(key)

        elif action == "hotkey":
            if len(sys.argv) < 3:
                raise ValueError('Format: py cli_pc.py hotkey "ctrl+s"')

            keys = sys.argv[2]
            result = hotkey(keys)

        elif action == "scroll":
            if len(sys.argv) < 3:
                raise ValueError("Format: py cli_pc.py scroll <amount>")

            amount = sys.argv[2]
            result = scroll(amount)

        elif action == "wait":
            if len(sys.argv) < 3:
                raise ValueError("Format: py cli_pc.py wait <seconds>")

            seconds = sys.argv[2]
            result = wait_seconds(seconds)

        elif action == "open_path":
            if len(sys.argv) < 3:
                raise ValueError('Format: py cli_pc.py open_path "<path>"')

            path = sys.argv[2]
            result = open_path(path)

        elif action == "open_app":
            if len(sys.argv) < 3:
                raise ValueError('Format: py cli_pc.py open_app "<app_name>"')

            app_name = sys.argv[2]
            result = open_app(app_name)

        elif action == "command":
            if len(sys.argv) < 3:
                raise ValueError('Format: py cli_pc.py command "<safe_command>"')

            command = sys.argv[2]
            result = run_safe_command(command)

        else:
            raise ValueError(f"Action tidak dikenal: {action}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_pc",
            "message": "Gagal menjalankan CLI PC Control",
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