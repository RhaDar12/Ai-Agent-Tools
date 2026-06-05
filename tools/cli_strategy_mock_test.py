import json
import sys

from strategy_mock_test_tool import run_strategy_mock_tests


def main():
    try:
        output_json = len(sys.argv) > 1 and sys.argv[1].lower().strip() == "--json"

        result = run_strategy_mock_tests()

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
            "tool": "cli_strategy_mock_test",
            "message": "Gagal menjalankan CLI strategy mock test",
            "error": str(e)
        }

        print(json.dumps(error_result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()