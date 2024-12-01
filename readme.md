
# QR Code JSON Encoder/Decoder For Contact Share

Generate a QR code containing contact information in JSON format and decode it back into a JSON object. The contact data includes details like ID, email, contact number, LinkedIn/GitHub URLs, organization, serial number, and SHA256 hash.

## Features

- **Random Contact Data Generation**: Uses the `Faker` library to generate random data for contact information.
- **JSON Encoding/Decoding**: Encodes the contact data into a JSON string and decodes it from the QR code.
- **QR Code Generation**: Generates a QR code that contains the JSON contact data.
- **QR Code Scanning**: Reads the QR code and decodes the JSON back into a dictionary.

![qr-code](qr-code.png =25x25)