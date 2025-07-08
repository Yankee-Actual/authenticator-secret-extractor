from pyzbar.pyzbar import decode
from PIL import Image
import urllib.parse

img = Image.open("qr.png")
result = decode(img)

if result:
    raw_data = result[0].data.decode()
    print("Raw QR Content:", raw_data)

    if raw_data.startswith("otpauth://"):
        parsed = urllib.parse.urlparse(raw_data)
        params = urllib.parse.parse_qs(parsed.query)

        secret = params.get("secret", [""])[0]
        issuer = params.get("issuer", ["Unknown"])[0]
        label = parsed.path.lstrip("/")

        print("Label   :", label)
        print("Issuer  :", issuer)
        print("Secret  :", secret)
    else:
        print("Not a valid OTP QR code.")
else:
    print("No QR code detected in the image.")
