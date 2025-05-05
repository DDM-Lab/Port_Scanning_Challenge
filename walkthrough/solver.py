import base64
import os

# Encoded text (replace with the actual encoded message)
full_encoded_message = "FIXME"

# Step 1: First Base64 decoding
decoded_once = base64.b64decode(FIXME)

# Step 2: Determine the script's directory
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decoded_image.png")  # Creates the full path for the image

# Step 3: Save as an image
with open(image_path, "wb") as image_file:
    image_file.write(decoded_once)

print("Image successfully decoded and saved as 'decoded_image.png'.")
