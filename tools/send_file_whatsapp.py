from pathlib import Path
import mimetypes
import requests

from core import (
    ensure_dirs,
    success_response,
    error_response,
    load_config
)

from delivered_file import mark_delivered, mark_failed


def guess_file_type(file_path):
    """
    Menentukan tipe file berdasarkan extension.
    Sesuai bridge Hermes: image, video, audio, document.
    """
    file_path = Path(file_path)
    ext = file_path.suffix.lower().replace(".", "")

    if ext in ["jpg", "jpeg", "png", "webp", "gif"]:
        return "image"

    if ext in ["mp4", "mov", "mkv", "avi", "webm"]:
        return "video"

    if ext in ["mp3", "wav", "ogg", "opus", "m4a"]:
        return "audio"

    return "document"


def send_file_whatsapp(file_path, target, caption="", delivery_id=None):
    """
    Mengirim file ke WhatsApp lewat Hermes whatsapp-bridge /send-media.

    Endpoint Hermes membutuhkan JSON:
    {
      "chatId": "...",
      "filePath": "...",
      "mediaType": "image|video|audio|document",
      "caption": "...",
      "fileName": "..."
    }
    """

    tool_name = "send_file_whatsapp"

    try:
        ensure_dirs()

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File tidak ditemukan: {file_path}")

        if not target:
            raise ValueError("Target WhatsApp kosong. Contoh: 628xxxxxxxxxx@s.whatsapp.net")

        config = load_config()
        wa_config = config.get("whatsapp_gateway", {})

        base_url = wa_config.get("base_url", "http://localhost:3000")
        endpoint = wa_config.get("send_file_endpoint", "/send-media")
        api_key = wa_config.get("api_key", "")

        url = base_url.rstrip("/") + endpoint

        mime_type, _ = mimetypes.guess_type(str(file_path))
        if mime_type is None:
            mime_type = "application/octet-stream"

        media_type = guess_file_type(file_path)

        headers = {
            "Content-Type": "application/json"
        }

        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        payload = {
            "chatId": target,
            "filePath": str(file_path),
            "mediaType": media_type,
            "caption": caption,
            "fileName": file_path.name
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=120
        )

        if response.status_code < 200 or response.status_code >= 300:
            error_msg = f"Gateway error {response.status_code}: {response.text}"

            if delivery_id:
                mark_failed(delivery_id, error_msg)

            raise RuntimeError(error_msg)

        if delivery_id:
            mark_delivered(delivery_id, sent_to=target)

        return success_response(
            tool=tool_name,
            message="File berhasil dikirim ke WhatsApp",
            file_path=file_path,
            extra={
                "target": target,
                "caption": caption,
                "media_type": media_type,
                "mime_type": mime_type,
                "gateway_url": url,
                "delivery_id": delivery_id,
                "gateway_response": response.text
            }
        )

    except Exception as e:
        if delivery_id:
            try:
                mark_failed(delivery_id, str(e))
            except Exception:
                pass

        return error_response(tool_name, e)