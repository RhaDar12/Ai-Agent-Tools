import json
import sys

from market_multi_alert_tool import send_multi_market_alert


def main():
    try:
        if len(sys.argv) < 4:
            raise ValueError(
                'Format: py cli_market_multi_alert.py "<news_status>" "XAUUSD=2.5,EURUSD=1.2,GBPUSD=1.5" "<chat_id>" [symbols_csv]'
            )

        news_status = sys.argv[1]
        spread_text = sys.argv[2]
        target = sys.argv[3]

        symbols = None
        if len(sys.argv) > 4 and sys.argv[4]:
            symbols = [s.strip().upper() for s in sys.argv[4].split(",") if s.strip()]

        result = send_multi_market_alert(
            news_status=news_status,
            spread_text=spread_text,
            target=target,
            symbols=symbols
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_multi_alert",
            "message": "Gagal menjalankan CLI multi market alert",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()