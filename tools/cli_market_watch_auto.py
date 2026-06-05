import json
import sys

from market_watch_auto_tool import run_market_watch_auto_news


def to_bool(value):
    if isinstance(value, bool):
        return value

    if value is None:
        return False

    return str(value).strip().lower() in ["1", "true", "yes", "y", "iya", "ya"]


def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError(
                'Format: py cli_market_watch_auto.py "XAUUSD=2.5,EURUSD=1.2,GBPUSD=1.5" "<chat_id>" [send_only_on_entry] [force_send] [news_window_minutes] [symbols_csv]'
            )

        spread_text = sys.argv[1]
        target = sys.argv[2]

        send_only_on_entry = to_bool(sys.argv[3]) if len(sys.argv) > 3 else True
        force_send = to_bool(sys.argv[4]) if len(sys.argv) > 4 else False
        news_window_minutes = int(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5] else 30

        symbols = None
        if len(sys.argv) > 6 and sys.argv[6]:
            symbols = [s.strip().upper() for s in sys.argv[6].split(",") if s.strip()]

        result = run_market_watch_auto_news(
            spread_text=spread_text,
            target=target,
            symbols=symbols,
            send_only_on_entry=send_only_on_entry,
            force_send=force_send,
            news_window_minutes=news_window_minutes
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_watch_auto",
            "message": "Gagal menjalankan CLI market watch auto-news",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()