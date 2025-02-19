from PIL import Image
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to encode message into image
def encode_image(image_path, secret_message):
    image = Image.open(image_path)
    encoded = image.copy()
    width, height = image.size
    pixels = np.array(encoded)
    
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message) + '1111111111111110'
    data_index = 0
    for row in pixels:
        for pixel in row:
            for channel in range(3):
                if data_index < len(binary_message):
                    pixel[channel] = pixel[channel] & ~1 | int(binary_message[data_index])
                    data_index += 1
    
    encoded_image = Image.fromarray(pixels)
    encoded_image.save("encoded_image.png")
    messagebox.showinfo("Success", "Message encoded successfully!")

# Function to decode message from image
def decode_image(image_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    binary_message = ''
    
    for row in pixels:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)
    
    byte_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = ''.join(chr(int(byte, 2)) for byte in byte_message if int(byte, 2) != 254)
    messagebox.showinfo("Decoded Message", decoded_message)

# GUI Application
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        secret_message = tk.simpledialog.askstring("Input", "Enter message to hide:")
        if secret_message:
            encode_image(file_path, secret_message)

def decode_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        decode_image(file_path)

root = tk.Tk()
root.withdraw()

choice = messagebox.askyesno("Steganography", "Do you want to encode a message?")
if choice:
    open_file()
else:
    decode_file()