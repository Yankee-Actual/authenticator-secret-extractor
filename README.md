# 🔐 Authenticator Secret Extractor

A lightweight Python toolset to extract OTP (TOTP/HOTP) secrets from QR codes.  
Supports both:
- 📦 Google Authenticator bulk export (`otpauth-migration://offline?...`)
- 🔹 Standard 2FA QR codes (`otpauth://totp/...`)

You can just install and securely back up your 2FA secrets for use in password managers like RoboForm, Bitwarden, or multi-device setups.

---

## 🧰 Included Scripts

### `decode_google_qr.py`
Used to decode **Google Authenticator's multi-account export QR codes**.

- Input: QR image exported from the Google Authenticator app.
- Output: Account name, issuer, and OTP secret in Base32 format.

✅ Handles the protobuf-based format used by Google.

---

### `extract_from_standard_qr.py`
Used to decode **individual OTP QR codes** shown during 2FA setup on most sites.

- Input: A standard QR image (e.g., from Okta, GitHub, AWS).
- Output: Secret key, label (email/username), and issuer.

✅ Works with most QR codes that follow the `otpauth://totp/...` format.

---

## 🖥️ Requirements

Install Python dependencies using:

```bash
pip install pillow pyzbar protobuf
📌 Additional System Dependency
You need the ZBar library installed for QR code scanning:

Windows:
choco install zbar
macOS:
brew install zbar
Debian/Ubuntu:
sudo apt install libzbar0

How to Use:
Save your QR screenshot as "qr.png" in the same folder as the script.

Run the appropriate script depending on the QR type:

For Google Authenticator Export QR:
python decode_google_qr.py
For Standard OTP QR:
python extract_from_standard_qr.py
The terminal will print the issuer, label (account/email), and the OTP secret.

🧪 Example Output:
✅ Found 1 account(s):

[1] GitHub - user@example.com
🔑 Secret: GAXG24DNNZ2W4Y3E...

🔒 Security Warning
Do NOT share or commit your OTP secrets.

Always store your secrets in an encrypted password manager or secure, offline storage (such as an encrypted USB drive).

This tool is intended for educational or personal backup use only.

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and share responsibly.
