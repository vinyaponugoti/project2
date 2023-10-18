#tmp
import os
import cv2

#update accordingly to match
directory = "/Users/justinbrady/Documents/UVA/Fall 23/DS Project Course/project2/DATA/low_contrast_test_set"

contrast_factor = 0.25

#looping over files in the directory
for filename in os.listdir(directory):
    #ensuring that the loop only gets the images that have not already been altered
    if(filename.find("_lowered_contrast") == -1):
        #loading the image
        file = os.path.join(directory, filename)
        image = cv2.imread(file)

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
        save_name = filename_without_extention + "_lowered_contrast.jpeg"
        save_path = os.path.join(directory, save_name)
        cv2.imwrite(save_path, adjusted_image)

        #removing the old version of the image
        os.remove(file)


