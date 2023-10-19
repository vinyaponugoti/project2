import os
import random
import shutil

def get_random_images(source_folder, destination_folder, num_images=10):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

        # Get a list of all files in the source folder
        all_files = os.listdir(source_folder)

        # Filter only .jpg files
        image_files = [f for f in all_files if f.lower().endswith('.jpg')]

        # Ensure that the number of requested images is not greater than the total number of images
        num_images = min(num_images, len(image_files))

        # Randomly select 'num_images' from the list
        selected_images = random.sample(image_files, num_images)

        # Copy selected images to the destination folder
        for image in selected_images:
            source_path = os.path.join(source_folder, image)
            destination_path = os.path.join(destination_folder, image)
            shutil.copyfile(source_path, destination_path)

# source_directory = "/Users/vinyaponugoti/Downloads/flickr30k-images"
# destination_directory = "DATA/images_set"
# number_of_images = 5

# get_random_images(source_directory, destination_directory, number_of_images)


def get_image_names(folder_path):
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Filter only image files (assumed to have extensions like .jpg)
    image_files = [f for f in all_files if f.lower().endswith(('.jpg'))]

    return image_files

def write_to_txt(image_names, txt_file_path):
    with open(txt_file_path, 'w') as file:
        for image_name in image_names:
            file.write(image_name + '\n')

# path to folder 
folder_path = "DATA/images_set"

# the desired path for the output text file
txt_file_path = "DATA/image_names.txt"

# image_names = get_image_names(folder_path)

# if image_names:
#     write_to_txt(image_names, txt_file_path)
#     print(f"Image names written to {txt_file_path}")
# else:
#     print("No image files found in the specified folder.")


def get_image_names_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def filter_caption_file(input_file_path, image_names, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            parts = line.strip().split(', ', 1)
            # if len(parts) == 2:
            image_name, caption = parts
            if image_name in image_names:
                output_file.write(line)

image_list_file_path = "DATA/image_names.txt"
caption_file_path = "DATA/flicker30k-captions.txt"
output_file_path = "DATA/output_file.txt"

# Get image names from the first file
# image_names = get_image_names_from_file(image_list_file_path)

# if image_names:
#     # Filter the caption file based on the image names
#     filter_caption_file(caption_file_path, image_names, output_file_path)
#     print(f"Filtered data written to {output_file_path}")
# else:
#     print("No image names found in the specified file.")





