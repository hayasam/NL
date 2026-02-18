
import base64

def upload_image(image_file):
    # Read the image file
    image_data = image_file.read()
    
    # Encode the image using base64
    encoded_image = base64.b64encode(image_data)
    
    # Write the encoded image to a file
    with open("encoded_image.txt", "wb") as f:
        f.write(encoded_image)
