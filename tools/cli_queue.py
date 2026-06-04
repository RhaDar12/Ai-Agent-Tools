import json
import sys

from message_queue import (
    add_message_to_queue,
    read_queue,
    mark_queue_processed
)


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                "Format: py cli_queue.py <add|read|processed> ..."
            )

        action = sys.argv[1]

        if action == "add":
            if len(sys.argv) < 4:
                raise ValueError(
                    "Format: py cli_queue.py add <chat_id> <message_text> [sender] [message_type] [file_path]"
                )

            chat_id = sys.argv[2]
            message_text = sys.argv[3]
            sender = sys.argv[4] if len(sys.argv) > 4 else None
            message_type = sys.argv[5] if len(sys.argv) > 5 else "text"
            file_path = sys.argv[6] if len(sys.argv) > 6 else None

            result = add_message_to_queue(
                chat_id=chat_id,
                message_text=message_text,
                sender=sender,
                message_type=message_type,
                file_path=file_path
            )

        elif action == "read":
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20
            status = sys.argv[3] if len(sys.argv) > 3 else None

            result = read_queue(
                limit=limit,
                status=status
            )

        elif action == "processed":
            if len(sys.argv) < 3:
                raise ValueError(
                    "Format: py cli_queue.py processed <queue_id>"
                )

            queue_id = sys.argv[2]
            result = mark_queue_processed(queue_id)

        else:
            raise ValueError(f"Action tidak dikenal: {action}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_queue",
            "message": "Gagal menjalankan CLI queue",
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