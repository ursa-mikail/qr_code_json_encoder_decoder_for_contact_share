#!pip install qrcode faker
import json
import qrcode
from faker import Faker
from PIL import Image
import cv2
import numpy as np

# Initialize Faker
fake = Faker()

# Generate random data
data = {
    "id": fake.uuid4(),
    "email": fake.email(),
    "contact_number": fake.phone_number(),
    "url.linkedin": fake.url(),
    "url.git": fake.url(),
    "org": fake.company(),
    "serial_number_org": fake.uuid4(),
    "hash_sha256": fake.sha256()
}

# Encode data to JSON
json_data = json.dumps(data, indent=4)
print("Generated JSON Data:\n", json_data)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qr_code.png")
print("QR code generated and saved as 'qr_code.png'")

# Display the QR code
img.show()

# Read the QR code image
img = Image.open("qr_code.png")

# Convert the image to a format OpenCV can work with
opencv_image = cv2.cvtColor(np.array(img.convert('RGB')), cv2.COLOR_RGB2BGR)

# Use OpenCV to decode the QR code
d = cv2.QRCodeDetector()
retval, points, straight_qrcode = d.detectAndDecode(opencv_image)

if retval:
    print("Decoded JSON Data:\n", retval)
    decoded_data = json.loads(retval)
    json_data = json.dumps(decoded_data, indent=4)
    print("Decoded JSON Object:\n", json_data)
else:
    print("QR Code could not be decoded")


"""
Generated JSON Data:
 {
    "id": "21659642-a101-4a17-a9ea-15807d1c4b1c",
    "email": "patrickalvarez@example.org",
    "contact_number": "+1-436-284-9329x9630",
    "url.linkedin": "https://rice-walker.net/",
    "url.git": "https://donaldson-davis.com/",
    "org": "Davidson PLC",
    "serial_number_org": "56c11393-4d0e-4525-93cc-41542c0445b7",
    "hash_sha256": "3dfc305165434fa92892e6ae7b4eab351dcc2e2422a123a361c59fb343ed8ff2"
}
QR code generated and saved as 'qr_code.png'
Decoded JSON Data:
 {
    "id": "21659642-a101-4a17-a9ea-15807d1c4b1c",
    "email": "patrickalvarez@example.org",
    "contact_number": "+1-436-284-9329x9630",
    "url.linkedin": "https://rice-walker.net/",
    "url.git": "https://donaldson-davis.com/",
    "org": "Davidson PLC",
    "serial_number_org": "56c11393-4d0e-4525-93cc-41542c0445b7",
    "hash_sha256": "3dfc305165434fa92892e6ae7b4eab351dcc2e2422a123a361c59fb343ed8ff2"
}
Decoded JSON Object:
 {
    "id": "21659642-a101-4a17-a9ea-15807d1c4b1c",
    "email": "patrickalvarez@example.org",
    "contact_number": "+1-436-284-9329x9630",
    "url.linkedin": "https://rice-walker.net/",
    "url.git": "https://donaldson-davis.com/",
    "org": "Davidson PLC",
    "serial_number_org": "56c11393-4d0e-4525-93cc-41542c0445b7",
    "hash_sha256": "3dfc305165434fa92892e6ae7b4eab351dcc2e2422a123a361c59fb343ed8ff2"
}
"""