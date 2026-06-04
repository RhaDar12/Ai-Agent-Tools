from pathlib import Path

from PIL import Image
from rembg import remove

from core import (
    DIRS,
    ensure_dirs,
    make_id,
    success_response,
    error_response
)

from delivered_file import create_delivery_record


def remove_background(
    image_path,
    target=None,
    caption="Gambar tanpa background dari AI-Agent"
):
    """
    Menghapus background dari gambar.
    Output: PNG transparan.
    """

    tool_name = "remove_background"

    try:
        ensure_dirs()

        image_path = Path(image_path)

        if not image_path.exists():
            raise FileNotFoundError(f"File gambar tidak ditemukan: {image_path}")

        output_id = make_id("bg_removed")
        output_path = DIRS["images"] / f"{output_id}.png"

        input_image = Image.open(image_path).convert("RGBA")
        output_image = remove(input_image)

        output_image.save(output_path)

        delivery = create_delivery_record(
            file_path=output_path,
            target=target,
            caption=caption
        )

        return success_response(
            tool=tool_name,
            message="Background berhasil dihapus",
            file_path=output_path,
            extra={
                "source_image_path": str(image_path),
                "output_id": output_id,
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