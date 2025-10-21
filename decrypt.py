from Crypto.Cipher import AES
from dotenv import load_dotenv
from stego_lsb.LSBSteg import recover_data
import os
import sys

def aes_decrypt(ciphertext: bytes, key: bytes) -> str:
    # load aes key from .env
    load_dotenv()
    nonce = ciphertext[:16]
    tag = ciphertext[16:32]
    actual_ciphertext = ciphertext[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(actual_ciphertext, tag)
    return data.decode()



def main():
    print("=== Extracting hidden data from steganographic image ===")
    
    # Get steganographic image location from command line argument or user input
    if len(sys.argv) > 1:
        stego_image = sys.argv[1]
    else:
        stego_image = input("Enter the path to the steganographic image (e.g., public/Encrypted_image.png): ").strip()
    
    # Validate image exists
    if not os.path.exists(stego_image):
        print(f"Error: Steganographic image '{stego_image}' not found.")
        return
    
    if not stego_image.lower().endswith(('.png', '.bmp')):
        print("Error: Image must be a .png or .bmp file.")
        return
    
    print(f"Using steganographic image: {stego_image}")
    
    # Extract the hidden encrypted data from the image
    output_file = 'public/recovered_encrypted_data.txt'
    num_lsb = 2  # Must match the value used during encryption
    
    print("Recovering hidden data from image...")
    recover_data(stego_image, output_file, num_lsb)
    print(f"Data recovered and saved to {output_file}")
    
    # Load AES key
    with open('.env', 'r') as f:
        lines = f.readlines()
    aes_key_line = next(line for line in lines if line.startswith('AES_KEY='))
    aes_key_hex = aes_key_line.strip().split('=')[1]
    key = bytes.fromhex(aes_key_hex)

    # Read the recovered encrypted data
    with open(output_file, 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data
    decrypted_data = aes_decrypt(encrypted_data, key)
    print("Decrypted data:", decrypted_data)

if __name__ == "__main__":
    main()