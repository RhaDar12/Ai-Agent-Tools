import json
import sys

from market_watch_tool import run_market_watch


def to_bool(value):
    if isinstance(value, bool):
        return value

    if value is None:
        return False

    return str(value).strip().lower() in ["1", "true", "yes", "y", "iya", "ya"]


def main():
    try:
        if len(sys.argv) < 4:
            raise ValueError(
                'Format: py cli_market_watch.py "<news_status>" "XAUUSD=2.5,EURUSD=1.2,GBPUSD=1.5" "<chat_id>" [send_only_on_entry] [force_send] [symbols_csv]'
            )

        news_status = sys.argv[1]
        spread_text = sys.argv[2]
        target = sys.argv[3]

        send_only_on_entry = to_bool(sys.argv[4]) if len(sys.argv) > 4 else True
        force_send = to_bool(sys.argv[5]) if len(sys.argv) > 5 else False

        symbols = None
        if len(sys.argv) > 6 and sys.argv[6]:
            symbols = [s.strip().upper() for s in sys.argv[6].split(",") if s.strip()]

        result = run_market_watch(
            news_status=news_status,
            spread_text=spread_text,
            target=target,
            symbols=symbols,
            send_only_on_entry=send_only_on_entry,
            force_send=force_send
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_watch",
            "message": "Gagal menjalankan CLI market watch",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()