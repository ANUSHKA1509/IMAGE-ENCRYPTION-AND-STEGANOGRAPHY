import numpy as np
from PIL import Image

def chaos_encrypt(image, r, x0):
    image_array = np.array(image)
    key = np.zeros_like(image_array, dtype=np.uint8)
    x = x0
    for i in range(key.size):
        x = r * x * (1 - x)
        key.flat[i] = int(x * 256)
    encrypted_array = np.bitwise_xor(image_array, key)
    encrypted_image = Image.fromarray(encrypted_array)
    return encrypted_image

def lsb_steganography(image, secret_image):
    image_array = np.array(image)
    secret_image_array = np.array(secret_image)
    stego_array = image_array & 0xFE
    secret_bits = secret_image_array >> 7
    stego_array = stego_array | secret_bits
    stego_image = Image.fromarray(stego_array)
    return stego_image

def chaos_decrypt(image, r, x0):
    image_array = np.array(image)
    key = np.zeros_like(image_array, dtype=np.uint8)
    x = x0
    for i in range(key.size):
        x = r * x * (1 - x)
        key.flat[i] = int(x * 256)
    decrypted_array = np.bitwise_xor(image_array, key)
    decrypted_image = Image.fromarray(decrypted_array)
    return decrypted_image

def lsb_steganography_extract(stego_image):
    stego_array = np.array(stego_image)
    secret_bits = stego_array & 0x01
    secret_image_array = secret_bits << 7
    secret_image = Image.fromarray(secret_image_array)
    return secret_image
