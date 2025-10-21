from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from stego_lsb.LSBSteg import hide_data
import os
import sys

def aes_encrypt(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def main():
    print("=== LSB Steganography Encryption ===")
    
    # Get image location from command line argument or user input
    if len(sys.argv) > 1:
        input_image = sys.argv[1]
    else:
        input_image = input("Enter the path to the image file (e.g., public/Normal_Image.png): ").strip()
    
    # Validate image exists and has correct extension
    if not os.path.exists(input_image):
        print(f"Error: Image file '{input_image}' not found.")
        return
    
    if not input_image.lower().endswith(('.png', '.bmp')):
        print("Error: Image must be a .png or .bmp file.")
        return
    
    print(f"Using image: {input_image}")
    
    plaintext = input("Enter data to encrypt: ")
    key = get_random_bytes(32)  
    with open('.env', 'w') as f:
        f.write(f"AES_KEY={key.hex()}\n")
    
    encrypted_data = aes_encrypt(plaintext.encode(), key)
    
    # Save encrypted data to a temporary file
    with open('public/encrypted_data.txt', 'wb') as f:
        f.write(encrypted_data)
    print("Data encrypted and saved to public/encrypted_data.txt")
    
    image_dir = os.path.dirname(input_image)
    image_filename = os.path.basename(input_image)
    output_image = os.path.join(image_dir, f"stego_{image_filename}")
    
    num_lsb = 2  # Number of least significant bits to use
    compression_level = 0  # PNG compression level (0-9)
    
    print(f"Hiding encrypted data in image using LSB steganography...")
    hide_data(input_image, 'public/encrypted_data.txt', output_image, num_lsb, compression_level)
    print(f"Steganography complete! Output saved to: {output_image}")
    print(f"You can now safely share {output_image} - the encrypted data is hidden inside!")

if __name__ == "__main__":
    main()