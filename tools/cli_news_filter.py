import json
import sys

from news_filter_tool import check_high_impact_news


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_news_filter.py <XAUUSD|EURUSD|GBPUSD> [window_minutes]'
            )

        symbol = sys.argv[1]
        window_minutes = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else 30

        result = check_high_impact_news(
            symbol=symbol,
            window_minutes=window_minutes
        )

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_news_filter",
            "message": "Gagal menjalankan CLI news filter",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()