import json
import sys

from market_debug_mt5_tool import build_mt5_debug_report


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError(
                'Format: py cli_market_debug_mt5.py <XAUUSD|EURUSD|GBPUSD> [--json]'
            )

        symbol = sys.argv[1]
        output_json = len(sys.argv) > 2 and sys.argv[2].lower().strip() == "--json"

        result = build_mt5_debug_report(symbol)

        if output_json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return

        report = result.get("report")

        if report:
            print(report)
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        error_result = {
            "success": False,
            "tool": "cli_market_debug_mt5",
            "message": "Gagal menjalankan CLI market debug MT5",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()