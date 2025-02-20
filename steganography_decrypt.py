import cv2
import os

def decrypt_message():
    # Read the encrypted image
    encrypted_img_name = input("Enter the name of the encrypted image file: ")
    img = cv2.imread(encrypted_img_name)
    if img is None:
        print("Error: Could not load encrypted image file")
        return
    
    # Get password from user
    input_password = input("Enter passcode for Decryption: ")
    
    # Read stored password
    try:
        with open("pass.txt", "r") as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found")
        return
    
    # Verify password
    if input_password != stored_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    # Create ASCII to character mapping
    c = {i: chr(i) for i in range(255)}
    
    # Get message length from first pixel
    msg_length = img[0, 0, 0] * 255 + img[0, 0, 1]
    
    # Decrypt the message
    message = ""
    n, m, z = 1, 0, 0  # Start from next pixel after length storage
    
    for i in range(msg_length):
        message += c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)

if __name__ == "__main__":
    decrypt_message()