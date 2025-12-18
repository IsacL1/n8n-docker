#!/usr/bin/env python3
import base64

def main():
    # The string to be encoded
    date = "bHZrIU8iR1aEtVpEdLgVOA:5hGgGOCme083TDsH6P2rhwVkwf8ERwo6"

    # Encode the string using Base64. The string is first encoded to bytes using UTF-8.
    encoded_bytes = base64.b64encode(date.encode("utf-8"))

    # Convert the encoded bytes back to a string for display
    encoded_str = str(encoded_bytes, "utf-8")
    print(encoded_str)

if __name__ == "__main__":
    main()