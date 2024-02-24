import base64

encoded_string = "=?utf-8?B?INCS0L7RgdC/0L7Qu9GM0LfQvtCy0LDRgtGM0YHRjyDQsdC+0L3Rg9GB0L4=?="
decoded_bytes = base64.b64decode(encoded_string.split("?B?")[1].split("?=")[0])
decoded_text = decoded_bytes.decode("utf-8")

print(decoded_text)