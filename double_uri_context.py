import urllib.parse


def double_url_encode(payload: str) -> str:
    # First encoding
    first = urllib.parse.quote(payload, safe='')

    # Second encoding
    second = urllib.parse.quote(first, safe='')

    return second


if __name__ == "__main__":
    user_input = input("Enter payload: ")

    result = double_url_encode(user_input)

    print("\n[+] Double Encoded Payload:")
    print(result)