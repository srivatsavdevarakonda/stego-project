## Overview
This project implements a secure image steganography system that allows users to hide text messages within images using pixel manipulation and password protection. The hidden messages are invisible to the naked eye and can only be extracted with the correct password.


## Features
- Text message encryption within images
- Password protection for message extraction
- No visible changes to the carrier image
- Separate encryption and decryption modules
- Support for JPG/PNG formats
- Dynamic message length handling

## Requirements
- Python 3.x
- OpenCV (cv2)
```bash
pip install opencv-python
```

## Project Structure
```
Image-Steganography/
│
├── steganography_encrypt.py
├── steganography_decrypt.py
├── IM.jpg                  # Sample input image
├── requirements.txt
    ```bash
    pip install -r requirements.txt
    ```
└── README.md
```

## How to Use

### 1. Encryption
```bash
python steganography_encrypt.py
```
- Input:
  - Original image file (JPG/PNG)
  - Secret message
  - Password
- Output:
  - Encrypted image (encrypted_message.png)
  - Password file (pass.txt)

### 2. Decryption
```bash
python steganography_decrypt.py
```
- Input:
  - Encrypted image name
  - Password
- Output:
  - Decrypted message

## How It Works

### Encryption Process
1. Load the carrier image
2. Get message and password from user
3. Convert message characters to ASCII values
4. Store message length in first pixel
5. Embed message across image pixels
6. Save encrypted image and password

### Decryption Process
1. Load encrypted image
2. Verify password
3. Extract message length from first pixel
4. Retrieve ASCII values from pixels
5. Convert ASCII to characters
6. Display decrypted message

## Sample Code Usage
```python
# Encryption
Enter secret message: Hello World!
Enter a passcode: mypass123

# Decryption
Enter the name of the encrypted image file: encrypted_message.png
Enter passcode for Decryption: mypass123
Decrypted message: Hello World!
```

## Limitations
- Image must be large enough to hold the message
- Only supports text messages currently
- Password stored locally

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Author
D SRIVATSAV (@srivatsavdevarakonda)

##License
This project is licensed under the MIT License - see the LICENSE file for details.