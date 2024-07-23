import cv2 # type: ignore
import numpy as np # type: ignore

def encrypt_image(input_image_path, output_image_path, key):
  """Encrypts an image using pixel manipulation.

  Args:
    input_image_path: Path to the input image.
    output_image_path: Path to save the encrypted image.
    key: A numerical key for the encryption process.
  """

  img = cv2.imread(input_image_path)
  height, width, channels = img.shape

  # Simple encryption: XOR with the key
  encrypted_img = np.zeros_like(img)
  for i in range(height):
    for j in range(width):
      encrypted_img[i, j] = img[i, j] ^ key

  cv2.imwrite(output_image_path, encrypted_img)

def decrypt_image(input_image_path, output_image_path, key):
  """Decrypts an image using pixel manipulation.

  Args:
    input_image_path: Path to the encrypted image.
    output_image_path: Path to save the decrypted image.
    key: The numerical key used for encryption.
  """

  img = cv2.imread(input_image_path)
  height, width, channels = img.shape

  # Decryption is the same as encryption for XOR
  decrypted_img = np.zeros_like(img)
  for i in range(height):
    for j in range(width):
      decrypted_img[i, j] = img[i, j] ^ key

  cv2.imwrite(output_image_path, decrypted_img)

# Example usage
input_image = "image.jpg"
output_encrypted = "encrypted.jpg"
output_decrypted = "decrypted.jpg"
key = 42

encrypt_image(input_image, output_encrypted, key)
decrypt_image(output_encrypted, output_decrypted, key)
