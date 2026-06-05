import requests

from core import (
    ensure_dirs,
    success_response,
    error_response,
    load_config
)


def get_whatsapp_messages():
    """
    Mengambil pesan masuk dari Hermes WhatsApp bridge.
    Endpoint yang ditemukan: GET /messages
    """

    tool_name = "get_whatsapp_messages"

    try:
        ensure_dirs()

        config = load_config()
        wa_config = config.get("whatsapp_gateway", {})

        base_url = wa_config.get("base_url", "http://localhost:3000")
        endpoint = wa_config.get("messages_endpoint", "/messages")

        url = base_url.rstrip("/") + endpoint

        response = requests.get(
            url,
            timeout=60
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise RuntimeError(
                f"Gateway error {response.status_code}: {response.text}"
            )

        try:
            messages = response.json()
        except Exception:
            messages = response.text

        return success_response(
            tool=tool_name,
            message="Pesan WhatsApp berhasil diambil",
            extra={
                "gateway_url": url,
                "messages": messages
            }
        )

    except Exception as e:
        return error_response(tool_name, e)