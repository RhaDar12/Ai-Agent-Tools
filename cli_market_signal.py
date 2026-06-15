import json
import sys

from liquidity_sweep_strategy import analyze_liquidity_sweep


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_market_signal.py <XAUUSD|EURUSD|GBPUSD> [news_status] [spread_pips]'
            )

        symbol = sys.argv[1]
        news_status = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else "Manual check required"
        spread_pips = float(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else None

        result = analyze_liquidity_sweep(
            symbol=symbol,
            news_status=news_status,
            spread_pips=spread_pips
        )

        output = result.get("output")

        if output:
            print(output)
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_signal",
            "message": "Gagal menjalankan CLI market signal",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False))


if __name__ == "__main__":
    main()