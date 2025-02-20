# StegoShield-Secure-Image-Based-Data-Hiding

## Overview
This project implements image-based steganography using Python. It allows users to hide and extract secret messages within image files using the Least Significant Bit (LSB) technique.

## Features
- Hide messages in image files without noticeable changes.
- Extract hidden messages from steganographic images.
- User-friendly GUI using Tkinter.
- Works on Windows, macOS, and Linux.

## Technologies Used
- **Python**
- **Libraries**: PIL (Pillow), NumPy, OpenCV, Tkinter

## Installation
```bash
# Clone the repository
git clone https://github.com/yashsahu2001/StegoShield-Secure-Image-Based-Data-Hiding.git
cd StegoShield-Secure-Image-Based-Data-Hiding

# Install dependencies
pip install pillow numpy opencv-python tk
```

## Usage
### Encoding a Message
1. Run the script.
2. Select an image file.
3. Enter a secret message.
4. The encoded image will be saved as `encoded_image.png`.

### Decoding a Message
1. Run the script.
2. Select an encoded image.
3. The hidden message will be displayed.

## Screenshots For steps for Running the codes

## Command Prompt
<img width="491" alt="image" src="https://github.com/user-attachments/assets/1757b0ae-024d-4fb9-b653-2af37c7659fd" />
Running the code using command prompt by using command
### python stego.py

### Original Image
![Test](https://github.com/user-attachments/assets/30ecb2a0-a864-4943-a4f4-7f08d0783965)

### For in Encrypting 
![GUI Window](https://github.com/user-attachments/assets/d59db3b9-42d4-4641-afb1-9aab87ce010a)
Ask when start running the code (By clicking Yes button)

Choose the image

![Text Box](https://github.com/user-attachments/assets/9913116c-2f2a-44b4-8d70-d77db7fd3bc5)
In this text Box write the message you want to hide

![Successfull Image](https://github.com/user-attachments/assets/70f35254-5012-4165-87a2-2c2ea2045cbd)
Successfully the image is Encrypted

### For Decrypting the Image

![GUI Window](https://github.com/user-attachments/assets/9b299212-91bf-445a-ab88-b9949b9f575b)
This window comes erery times when you execute the code For Decrypt(By clicking No button)

![encoded_image](https://github.com/user-attachments/assets/f39c1f32-9e56-4238-b4c6-d12afa5ef6fe)
Choose the encoded_image to decrypt

![Decoded Image](https://github.com/user-attachments/assets/623c8082-e662-4fea-a647-c121865243f1)
Then the message you have given at the beginning it will show

## Future Scope
- Support for video and audio steganography.
- Integration with encryption techniques.
- Mobile application development.
- Cloud-based steganography.
- Resistance to steganalysis.

## License
This project is licensed under the MIT License.

## Contribution
Feel free to submit issues or pull requests to improve this project.

## Author
[Yash Sahu](https://github.com/yashsahu2001)
