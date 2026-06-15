from screenshot_pc import take_screenshot, take_screenshot_region

print("=== TEST FULL SCREENSHOT ===")

result = take_screenshot(
    target="628xxxxxxxxxx@s.whatsapp.net",
    caption="Test screenshot dari AI-Agent"
)

print(result)

print("\n=== TEST REGION SCREENSHOT ===")

region_result = take_screenshot_region(
    x=0,
    y=0,
    width=800,
    height=500,
    target="628xxxxxxxxxx@s.whatsapp.net",
    caption="Test screenshot region dari AI-Agent"
)

print(region_result)