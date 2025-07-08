# Google Authenticator QR Extractor

A simple Python script to extract OTP secrets from Google Authenticator export QR codes.

📦 Supports: `otpauth-migration://offline?data=...`

## Usage

1. Export your Google Authenticator accounts as QR
2. Save the image as `okta_qr.png` in the same folder
3. Run:

```bash
pip install pillow pyzbar protobuf
python decode_google_qr.py