import os
from PIL import Image

# Define the folder path
folder_path = '..\\DATA\\black_and_white_test_set\\'

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a JPG
    if file_name.endswith('.JPEG'):
        #print("if statement passes")
        # Create a full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Load the image
        with Image.open(file_path) as img:
            #convert to black and white using pillow
            img_gray = img.convert('L')

            # Save the rotated image (overwriting the original or to a new location)
            img_gray.save(os.path.join(folder_path, 'bw_' + file_name))
            #removing old images
        os.remove(file_path)