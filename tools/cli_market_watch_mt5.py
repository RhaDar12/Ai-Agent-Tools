import json
import sys

from market_watch_mt5_tool import run_market_watch_mt5


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
                'Format: py cli_market_watch_mt5.py "<chat_id>" [send_only_on_entry] [force_send] [symbols_csv]'
            )

        target = sys.argv[1]
        send_only_on_entry = to_bool(sys.argv[2]) if len(sys.argv) > 2 else True
        force_send = to_bool(sys.argv[3]) if len(sys.argv) > 3 else False

        symbols = None
        if len(sys.argv) > 4 and sys.argv[4]:
            symbols = [s.strip().upper() for s in sys.argv[4].split(",") if s.strip()]

        result = run_market_watch_mt5(
            target=target,
            symbols=symbols,
            send_only_on_entry=send_only_on_entry,
            force_send=force_send
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_watch_mt5",
            "message": "Gagal menjalankan CLI MT5 market watch",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()