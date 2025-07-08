# 2FA OTP Secret Extractor

This is a lightweight Python utility designed to securely extract OTP secrets from 2FA QR codes. It supports both standard TOTP QR codes and Google Authenticator’s export format. The tool operates fully offline and was built with a focus on privacy, control, and recoverability.

## Features

- Extract OTP secrets from:
  - Standard 2FA setup QR codes (`otpauth://totp?...`)
  - Google Authenticator export QR codes (`otpauth-migration://offline?...`)
- Completely offline processing (no API calls or cloud sync)
- Helpful for device loss scenarios or migrating 2FA to a trusted password manager

## Use Cases

- Backup OTP secrets in secure local storage
- Migrate OTP tokens to another device or authenticator app
- Recover account access when the original device is lost

## Requirements

- Python 3.7+
- `pyzbar`
- `Pillow`
- `protobuf`

Install requirements:

```bash
pip install -r requirements.txt

Usage
Save your QR code as a qr.png file

Run the script:

For standard OTP QR codes:
python extract_standard_qr.py

For Google Authenticator export QR codes:
python decode_google_qr.py

The tool will display the extracted secret, issuer, and label.

Disclaimer
This project was built independently using publicly documented formats and open libraries. No third-party code under restrictive licenses was used. It is intended for personal use or education only. Please ensure you handle all extracted secrets securely.
