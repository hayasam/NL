
import base64

def upload_image(image_path, output_file_path):
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        
        with open(output_file_path, 'w') as output_file:
            output_file.write(encoded_image)
        
        return True
    except Exception as e:
        print(f"Error processing image: {e}")
        return False
