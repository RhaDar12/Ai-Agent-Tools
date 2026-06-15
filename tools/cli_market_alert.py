import json
import sys

from market_alert_tool import send_market_signal_alert


def main():
    try:
        if len(sys.argv) < 5:
            raise ValueError(
                'Format: py cli_market_alert.py <XAUUSD|EURUSD|GBPUSD> "<news_status>" <spread_pips> "<chat_id>"'
            )

        symbol = sys.argv[1]
        news_status = sys.argv[2]
        spread_pips = float(sys.argv[3]) if sys.argv[3] else None
        target = sys.argv[4]

        result = send_market_signal_alert(
            symbol=symbol,
            news_status=news_status,
            spread_pips=spread_pips,
            target=target
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_alert",
            "message": "Gagal menjalankan CLI market alert",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()