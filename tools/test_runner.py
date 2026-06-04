from tool_runner import run_tool


print("=== TEST RUNNER SCREENSHOT ===")

result = run_tool(
    script_name="cli_screenshot.py",
    args=[
        "full",
        "628xxxxxxxxxx@s.whatsapp.net",
        "Screenshot dari tool_runner"
    ]
)

print(result)