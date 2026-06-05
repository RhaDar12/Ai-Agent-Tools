import json
import sys

from mt5_liquidity_sweep_strategy import analyze_liquidity_sweep_mt5


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_market_signal_mt5.py <XAUUSD|EURUSD|GBPUSD>'
            )

        symbol = sys.argv[1]

        result = analyze_liquidity_sweep_mt5(symbol)

        output = result.get("output")

        if output:
            print(output)
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_signal_mt5",
            "message": "Gagal menjalankan CLI market signal MT5",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()