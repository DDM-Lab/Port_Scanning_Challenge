import base64

# Original message
message = "Hello, World!"

# First encoding
encoded_once = base64.b64encode(message.encode()).decode()
print("First Base64 Encoding:", encoded_once)

# Second encoding
encoded_twice = base64.b64encode(encoded_once.encode()).decode()
print("Second Base64 Encoding:", encoded_twice)

# First decoding
decoded_once = base64.b64decode(encoded_twice).decode()
print("First Decoding:", decoded_once)

# Second decoding
decoded_twice = base64.b64decode(decoded_once).decode()
print("Final Decoded Message:", decoded_twice)
