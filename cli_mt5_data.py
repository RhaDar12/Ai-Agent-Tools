import json
import sys

from mt5_data_tool import (
    get_mt5_tick,
    get_mt5_ohlc,
    get_mt5_market_bundle
)


def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError(
                'Format: py cli_mt5_data.py <tick|ohlc|bundle> <symbol> [timeframe] [bars]'
            )

        action = sys.argv[1]
        symbol = sys.argv[2]

        if action == "tick":
            result = get_mt5_tick(symbol)

        elif action == "ohlc":
            timeframe = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "H1"
            bars = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] else 200

            result = get_mt5_ohlc(
                symbol=symbol,
                timeframe=timeframe,
                bars=bars
            )

        elif action == "bundle":
            result = get_mt5_market_bundle(symbol)

        else:
            raise ValueError(f"Action tidak dikenal: {action}")

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_mt5_data",
            "message": "Gagal menjalankan CLI MT5 data",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()