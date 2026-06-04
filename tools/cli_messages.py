import json
from whatsapp_messages import get_whatsapp_messages


def main():
    result = get_whatsapp_messages()
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()