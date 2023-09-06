import requests
import shutil

image_url = "https://drive.google.com/uc?export=download&id=1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF&confirm=t&uuid=64cae578-9fb6-4299-894d-514373c6492e&at=AB6BwCCnz6n3-mZ71VWveaeMYGkJ:1694009347128"    
response = requests.get(image_url, stream=True)

if response.status_code == 200:
    # Get the content of the response
    image_data = response.content
    
    # Define the local file path where you want to save the image
    local_file_path = "RoopNoFilter\\models\\inswapper_128.onnx"  # You can change the file name and extension
    
    # Save the image to your local directory
    with open(local_file_path, "wb") as image_file:
        image_file.write(image_data)
        
       
