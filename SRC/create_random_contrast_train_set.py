#tmp
import os
import cv2
import random

#update accordingly to match
directory = "/Users/justinbrady/Downloads/flickr30k-images"

#looping over files in the directory
for filename in os.listdir(directory):
    #ensuring that the loop only gets the images that have not already been altered
    if(filename.find("_random_contrast") == -1 and filename.find(".jpg") != -1):
        #loading the image
        file = os.path.join(directory, filename)
        image = cv2.imread(file)

        #generating random contrast factor between .25 and 1
        contrast_factor = (random.random() * 0.75) + 0.25

        #lowering its contrast to the value of contrast_factor
        adjusted_image = cv2.convertScaleAbs(image, alpha = contrast_factor)

        #creating a string without the file extension
        last_dot_index = filename.rfind(".")
        filename_without_extention = ""
        if last_dot_index != -1:
            filename_without_extention = filename[:last_dot_index]
        else:
            filename_without_extention = filename

        #saving the new image to the directory
        save_name = filename_without_extention + "_random_contrast.jpeg"
        save_path = os.path.join(directory, save_name)
        cv2.imwrite(save_path, adjusted_image)

        #removing the old version of the image
        os.remove(file)


