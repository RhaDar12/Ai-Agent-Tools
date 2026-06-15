import json
import subprocess
from pathlib import Path


TOOLS_DIR = Path("C:/AI-Agent/tools")


def run_tool(script_name, args=None, timeout=120):
    """
    Menjalankan tool AI-Agent menggunakan command py.
    Cocok dipanggil dari Hermes venv.
    """

    if args is None:
        args = []

    script_path = TOOLS_DIR / script_name

    if not script_path.exists():
        return {
            "success": False,
            "tool": "tool_runner",
            "message": "Script tool tidak ditemukan",
            "file_path": None,
            "delivered_file": {
                "status": "failed",
                "sent_to": None,
                "sent_at": None,
                "delivery_id": None
            },
            "error": f"Script tidak ditemukan: {script_path}"
        }

    try:
        command = ["py", str(script_path)] + [str(arg) for arg in args]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.returncode != 0:
            return {
                "success": False,
                "tool": "tool_runner",
                "message": "Tool gagal dijalankan",
                "file_path": None,
                "delivered_file": {
                    "status": "failed",
                    "sent_to": None,
                    "sent_at": None,
                    "delivery_id": None
                },
                "error": result.stderr.strip() or result.stdout.strip()
            }

        output = result.stdout.strip()

        if not output:
            return {
                "success": False,
                "tool": "tool_runner",
                "message": "Tool tidak mengembalikan output",
                "file_path": None,
                "delivered_file": {
                    "status": "failed",
                    "sent_to": None,
                    "sent_at": None,
                    "delivery_id": None
                },
                "error": "stdout kosong"
            }

        return json.loads(output)

    except json.JSONDecodeError as e:
        return {
            "success": False,
            "tool": "tool_runner",
            "message": "Output tool bukan JSON valid",
            "file_path": None,
            "delivered_file": {
                "status": "failed",
                "sent_to": None,
                "sent_at": None,
                "delivery_id": None
            },
            "error": str(e)
        }

    except Exception as e:
        return {
            "success": False,
            "tool": "tool_runner",
            "message": "Terjadi error saat menjalankan tool",
            "file_path": None,
            "delivered_file": {
                "status": "failed",
                "sent_to": None,
                "sent_at": None,
                "delivery_id": None
            },
            "error": str(e)
        }