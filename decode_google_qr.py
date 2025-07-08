import base64
import urllib.parse
from pyzbar.pyzbar import decode
from PIL import Image
from google.protobuf import descriptor_pb2, descriptor_pool, message_factory, message
import os

pool = descriptor_pool.Default()
file_desc_proto = descriptor_pb2.FileDescriptorProto()
file_desc_proto.name = "migration.proto"
file_desc_proto.package = "auth"

file_desc_proto.message_type.add(
    name="MigrationPayload",
    field=[
        descriptor_pb2.FieldDescriptorProto(name="otp_parameters", number=1, label=3, type=11, type_name="auth.OTPParameters"),
        descriptor_pb2.FieldDescriptorProto(name="version", number=2, label=1, type=5),
        descriptor_pb2.FieldDescriptorProto(name="batch_size", number=3, label=1, type=5),
        descriptor_pb2.FieldDescriptorProto(name="batch_index", number=4, label=1, type=5),
        descriptor_pb2.FieldDescriptorProto(name="batch_id", number=5, label=1, type=5),
    ]
)

file_desc_proto.message_type.add(
    name="OTPParameters",
    field=[
        descriptor_pb2.FieldDescriptorProto(name="secret", number=1, label=1, type=12),
        descriptor_pb2.FieldDescriptorProto(name="name", number=2, label=1, type=9),
        descriptor_pb2.FieldDescriptorProto(name="issuer", number=3, label=1, type=9),
        descriptor_pb2.FieldDescriptorProto(name="algorithm", number=4, label=1, type=14, type_name="auth.Algorithm"),
        descriptor_pb2.FieldDescriptorProto(name="digits", number=5, label=1, type=14, type_name="auth.Digits"),
        descriptor_pb2.FieldDescriptorProto(name="type", number=6, label=1, type=14, type_name="auth.OTPType"),
        descriptor_pb2.FieldDescriptorProto(name="counter", number=7, label=1, type=4),
    ]
)

file_desc_proto.enum_type.add(
    name="Algorithm",
    value=[
        descriptor_pb2.EnumValueDescriptorProto(name="ALGORITHM_UNSPECIFIED", number=0),
        descriptor_pb2.EnumValueDescriptorProto(name="ALGORITHM_SHA1", number=1),
        descriptor_pb2.EnumValueDescriptorProto(name="ALGORITHM_SHA256", number=2),
        descriptor_pb2.EnumValueDescriptorProto(name="ALGORITHM_SHA512", number=3),
        descriptor_pb2.EnumValueDescriptorProto(name="ALGORITHM_MD5", number=4),
    ]
)

file_desc_proto.enum_type.add(
    name="Digits",
    value=[
        descriptor_pb2.EnumValueDescriptorProto(name="DIGITS_UNSPECIFIED", number=0),
        descriptor_pb2.EnumValueDescriptorProto(name="DIGITS_SIX", number=1),
        descriptor_pb2.EnumValueDescriptorProto(name="DIGITS_EIGHT", number=2),
    ]
)

file_desc_proto.enum_type.add(
    name="OTPType",
    value=[
        descriptor_pb2.EnumValueDescriptorProto(name="OTP_TYPE_UNSPECIFIED", number=0),
        descriptor_pb2.EnumValueDescriptorProto(name="HOTP", number=1),
        descriptor_pb2.EnumValueDescriptorProto(name="TOTP", number=2),
    ]
)

file_desc = pool.Add(file_desc_proto)
MigrationPayloadDescriptor = pool.FindMessageTypeByName("auth.MigrationPayload")
MigrationPayload = message_factory.GetMessageClass(MigrationPayloadDescriptor)

img_path = "qr.png"
if not os.path.exists(img_path):
    print(f"❌ Image '{img_path}' not found.")
    exit()

img = Image.open(img_path)
result = decode(img)

if not result:
    print("❌ No QR code detected.")
    exit()

raw_data = result[0].data.decode()
if not raw_data.startswith("otpauth-migration://offline?data="):
    print("❌ Not a valid Google Authenticator QR export.")
    exit()

parsed = urllib.parse.urlparse(raw_data)
params = urllib.parse.parse_qs(parsed.query)

try:
    binary_data = base64.urlsafe_b64decode(params["data"][0])
    payload = MigrationPayload()
    payload.ParseFromString(binary_data)

    print(f"\n✅ Found {len(payload.otp_parameters)} account(s):\n")
    for i, otp in enumerate(payload.otp_parameters, 1):
        secret = base64.b32encode(otp.secret).decode("utf-8")
        name = otp.name or "Unnamed"
        issuer = otp.issuer or "Unknown"
        print(f"[{i}] {issuer} - {name}")
        print(f"🔑 Secret: {secret}\n")
except Exception as e:
    print("❌ Error decoding data:", e)
