# 🔐 LSB Steganography with AES Encryption

A Python-based steganography tool that combines **AES-256 encryption** with **LSB (Least Significant Bit) steganography** to securely hide encrypted messages inside images.

## 📋 Overview

This project allows you to:
1. **Encrypt** sensitive data using AES-256 encryption
2. **Hide** the encrypted data inside PNG/BMP images using LSB steganography
3. **Extract** and **decrypt** the hidden data from steganographic images

The hidden data is virtually undetectable to the human eye, making this a secure way to transmit sensitive information.

## 🚀 Features

- **AES-256 Encryption**: Military-grade encryption for your data
- **LSB Steganography**: Hides encrypted data in image pixels
- **Flexible Image Input**: Specify image paths via command-line or interactive prompt
- **Support for PNG and BMP**: Works with common image formats
- **Automatic Key Management**: AES keys are securely stored in `.env` file
- **Easy to Use**: Simple command-line interface

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install pycryptodome python-dotenv stego-lsb pillow
   ```

## 🎯 Usage

### Encrypting and Hiding Data

You can encrypt and hide data in an image using two methods:

**Method 1: Command-line argument**
```bash
python encrypt.py path/to/your/image.png
```

**Method 2: Interactive prompt**
```bash
python encrypt.py
# Then enter the image path when prompted
```

**Example:**
```bash
python encrypt.py public/Normal_Image.png
# Enter your secret message when prompted
# Output: public/stego_Normal_Image.png
```

### Extracting and Decrypting Data

You can extract and decrypt hidden data using two methods:

**Method 1: Command-line argument**
```bash
python decrypt.py path/to/stego_image.png
```

**Method 2: Interactive prompt**
```bash
python decrypt.py
# Then enter the steganographic image path when prompted
```

**Example:**
```bash
python decrypt.py public/stego_Normal_Image.png
# The original secret message will be displayed
```

## 📁 Project Structure

```
stego/
├── encrypt.py                 # Encryption and hiding script
├── decrypt.py                 # Extraction and decryption script
├── .env                       # AES encryption key (auto-generated)
├── README.md                  # This file
├── public/                    # Directory for images and data
│   ├── encrypted_data.txt     # Temporary encrypted data file
│   └── recovered_encrypted_data.txt  # Recovered encrypted data
└── venv/                      # Virtual environment (optional)
```

## 🔧 How It Works

### Encryption Process (`encrypt.py`)

1. **Input**: Takes an image file and your secret message
2. **AES Encryption**: Encrypts the message using AES-256-EAX mode
3. **Key Storage**: Saves the encryption key to `.env` file
4. **Temporary Storage**: Saves encrypted data to `public/encrypted_data.txt`
5. **LSB Steganography**: Hides the encrypted data in the least significant bits of image pixels
6. **Output**: Creates a steganographic image with prefix `stego_`

### Decryption Process (`decrypt.py`)

1. **Input**: Takes a steganographic image
2. **Data Recovery**: Extracts hidden data from image pixels using LSB extraction
3. **Key Loading**: Reads the AES key from `.env` file
4. **AES Decryption**: Decrypts the recovered data using AES-256
5. **Output**: Displays the original secret message

## ⚙️ Configuration

### LSB Parameters

In both `encrypt.py` and `decrypt.py`, you can adjust:

- `num_lsb = 2`: Number of least significant bits used (1-8)
  - Lower values = Better image quality, less capacity
  - Higher values = More capacity, potentially visible artifacts
  
- `compression_level = 0`: PNG compression level (0-9)
  - 0 = No compression (faster, larger files)
  - 9 = Maximum compression (slower, smaller files)

### Supported Image Formats

- **PNG** (Portable Network Graphics) - Recommended
- **BMP** (Bitmap) - Also supported

## 🔒 Security Considerations

- **Keep `.env` file secure**: It contains your encryption key
- **Never share `.env` file**: Only share the steganographic image
- **Use strong passphrases**: If extending this project with password-based encryption
- **Image Quality**: The steganographic image is visually identical to the original

## 📝 Example Workflow

```bash
# 1. Encrypt and hide your message
$ python encrypt.py public/vacation_photo.png
Enter data to encrypt: Meet me at the park at 3pm
# Output: public/stego_vacation_photo.png

# 2. Share the stego image (looks like a normal photo!)
# The recipient needs your .env file to decrypt

# 3. Decrypt and extract the message
$ python decrypt.py public/stego_vacation_photo.png
# Output: Meet me at the park at 3pm
```

## 🛠️ Troubleshooting

### Common Issues

**"Image file not found"**
- Check that the file path is correct
- Use relative paths from the project directory

**"Image must be a .png or .bmp file"**
- Convert your image to PNG or BMP format
- Most image editors support this conversion

**"Only able to hide X bytes"**
- Your message is too large for the image
- Use a larger image or reduce message size
- Increase `num_lsb` value (may affect image quality)

**"AES_KEY not found in .env"**
- Run `encrypt.py` first to generate the key
- Ensure `.env` file exists in the project root

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

## ⚠️ Disclaimer

This tool is for educational purposes. Always ensure you comply with local laws and regulations when using encryption and steganography tools.
