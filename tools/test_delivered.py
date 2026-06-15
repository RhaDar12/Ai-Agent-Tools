from delivered_file import (
    create_delivery_record,
    mark_delivered,
    mark_failed,
    get_delivery_record
)


file_path = "C:/AI-Agent/outputs/documents/test.txt"
target = "628xxxxxxxxxx@s.whatsapp.net"
caption = "Ini file test dari AI-Agent"

print("=== CREATE DELIVERY RECORD ===")
result = create_delivery_record(
    file_path=file_path,
    target=target,
    caption=caption
)

print(result)

delivery_id = result.get("delivery_id")

if delivery_id:
    print("\n=== GET DELIVERY RECORD ===")
    record = get_delivery_record(delivery_id)
    print(record)

    print("\n=== MARK DELIVERED ===")
    delivered = mark_delivered(
        delivery_id=delivery_id,
        sent_to=target
    )
    print(delivered)
else:
    print("Delivery ID tidak ditemukan, test berhenti.")