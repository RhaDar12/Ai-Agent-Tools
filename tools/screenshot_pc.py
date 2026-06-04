from pathlib import Path
import pyautogui

from core import (
    DIRS,
    ensure_dirs,
    make_id,
    success_response,
    error_response
)

from delivered_file import create_delivery_record


def take_screenshot(target=None, caption="Screenshot dari PC"):
    """
    Mengambil screenshot layar PC dan membuat delivery record.
    """
    tool_name = "take_screenshot"

    try:
        ensure_dirs()

        screenshot_id = make_id("screenshot")
        file_path = DIRS["screenshots"] / f"{screenshot_id}.png"

        image = pyautogui.screenshot()
        image.save(file_path)

        delivery = create_delivery_record(
            file_path=file_path,
            target=target,
            caption=caption
        )

        return success_response(
            tool=tool_name,
            message="Screenshot berhasil dibuat",
            file_path=file_path,
            extra={
                "screenshot_id": screenshot_id,
                "delivery_id": delivery.get("delivery_id"),
                "delivery_record": delivery.get("delivery_record"),
                "delivered_file": {
                    "status": "pending",
                    "sent_to": target,
                    "sent_at": None,
                    "delivery_id": delivery.get("delivery_id")
                }
            }
        )

    except Exception as e:
        return error_response(tool_name, e)


def take_screenshot_region(x, y, width, height, target=None, caption="Screenshot region dari PC"):
    """
    Mengambil screenshot area tertentu.
    x, y = posisi awal
    width, height = ukuran area
    """
    tool_name = "take_screenshot_region"

    try:
        ensure_dirs()

        screenshot_id = make_id("screenshot_region")
        file_path = DIRS["screenshots"] / f"{screenshot_id}.png"

        image = pyautogui.screenshot(region=(x, y, width, height))
        image.save(file_path)

        delivery = create_delivery_record(
            file_path=file_path,
            target=target,
            caption=caption
        )

        return success_response(
            tool=tool_name,
            message="Screenshot region berhasil dibuat",
            file_path=file_path,
            extra={
                "screenshot_id": screenshot_id,
                "region": {
                    "x": x,
                    "y": y,
                    "width": width,
                    "height": height
                },
                "delivery_id": delivery.get("delivery_id"),
                "delivery_record": delivery.get("delivery_record"),
                "delivered_file": {
                    "status": "pending",
                    "sent_to": target,
                    "sent_at": None,
                    "delivery_id": delivery.get("delivery_id")
                }
            }
        )

    except Exception as e:
        return error_response(tool_name, e)