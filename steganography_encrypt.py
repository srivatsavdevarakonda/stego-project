import cv2
import os
import string

def encrypt_message():
    # Read the image
    img = cv2.imread("IM.jpg")  # Make sure to have this image in the same directory
    if img is None:
        print("Error: Could not load image file")
        return
    
    # Get message and password from user
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    # Create character to ASCII mapping
    d = {chr(i): i for i in range(255)}
    
    # Embed the message length and password for later verification
    # Store message length in first pixel
    msg_length = len(msg)
    img[0, 0, 0] = msg_length // 255
    img[0, 0, 1] = msg_length % 255
    
    # Encrypt and embed the message
    n, m, z = 1, 0, 0  # Start from next pixel after length storage
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    # Save both the encrypted image and password
    encrypted_img_name = "encrypted_message.png"
    cv2.imwrite(encrypted_img_name, img)
    
    # Save password to a separate file
    with open("pass.txt", "w") as f:
        f.write(password)
    
    print(f"Message encrypted successfully!")
    print(f"Encrypted image saved as: {encrypted_img_name}")
    print("Password has been saved to pass.txt")
    
    # Display the encrypted image
    os.system(f"start {encrypted_img_name}")  # For Windows
    # For Linux/Mac, comment above line and uncomment below line
    # os.system(f"open {encrypted_img_name}")

if __name__ == "__main__":
    encrypt_message()