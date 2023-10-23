# DS Project Course Project 2

# SRC 
### Code installation
Ensure that you have python3 installed on your computer. While not required, it is also suggested that you run the following installation commands within a python virtual environment. Information about setting up a virtual environment can be found [here](https://docs.python.org/3/library/venv.html).

To install this code make sure to install the following packages:
- ```pip install Pillow```
- ```pip install opencv-python```
- ```pip install tensorflow```
- ```pip install keras```
- ```pip install numpy```
- ```pip install tqdm```
- ```pip install jupyterlab```
- ```pip install pydot```
- ```pip install graphviz```
- ```pip install pandas```
- ```pip install matplotlib```

### Code usage
#### Model Training
To train the model, first download the train set you would like to use. In `caption_generator.py` change the `dataset_images` variable to the the filepath to the folder with the images. After that, change the `filename` at lines 82 and 151 to match the captions and trainimages files that correspond with the images dataset. Once these updates have been made, run the code using `python3 SRC/caption_generator.py`. Note the code make many hours to run, a powerful CPU or GPU is strongly reccomended when training this model. 

#### Model Testing
In order to generate captions for images using our model, use the command ```python3 SRC/testing_generator.py``` This will output the test results for the images from the well lit, black and white, and low contrast datasets into the well_lit_results.csv, black_white_results.csv, and low_contrast_results.csv respectively with each image from the dataset and its generated caption in the same line. In order to generate captions for a new dataset of images you can add ```save_test_results("name_of_images_dataset", "output.csv")``` to the end of the ```testing_generator.py``` file and change the ```max_length``` variable in ```testing_generator.py``` file (around line 79) to the expected shape size if a ValueError occurs. The generated captions for each image can then be viewed in the ```output.csv``` file.


# DATA
Within our data folder, there are three subfolders which contain our three test sets. Each subfolder contains 100 images that can be used by `testing_generator.py` to create captions for analysis of the model. `flicker30k-captions.txt` and `flickr30k-random-contrast-captions.txt` contain the set of image names with each of their 5 corresponding captions which is used in training the model. `Flickr_30k.trainImages.txt` and `flickr30k-random-contrast-trainImages.txt` is a newline separated list of each of the image names inthe flickr30k dataset which is needed for training the model. The main Flikr30k images dataset and the random contrast version of the set do not fit on github due to their size, so they can be accessed from our google drive data folder [here](https://drive.google.com/drive/folders/1ye6XsPeA9_LKVxbcmmriqXtG1ADnkz-F?usp=sharing). The two image files on the google drive are named `flickr30k-images.tar.gz` and `flickr30k-random-contrastimages.zip`. Both of these image sets contain the same 30,000 images. The random contrast dataset has modified the original flikr30k set to have random contrast on the images. The code for this change can be seen in `create_random_contrast_train_set.py`.

## Data Dictionary
| Attribute Name | Data Type | Required | Description | Example |
| -------------- | --------- | ------- | ----------- | ------- |
| Photo ID Number | Integer | Yes | The number associated with each photo or image | “4576671” |
| Caption 1 | String | Yes | Contains the file name and then followed by the caption for the image | “1000092795.jpg, Two young guys with shaggy hair look at their hands while hanging out in the yard .” |
| Caption 2 | String | Yes | Contains the file name and then followed by the caption for the image | “1000092795.jpg," Two young , White males are outside near many bushes ." |
| Caption 3 | String | Yes | Contains the file name and then followed by the caption for the image | “1000092795.jpg, Two men in green shirts are standing in a yard.” |
| Caption 4 | String | Yes | Contains the file name and then followed by the caption for the image | “1000092795.jpg, A man in a blue shirt standing in a garden .” |
| Caption 5 | String | Yes | Contains the file name and then followed by the caption for the image | “1000092795.jpg,  Two friends enjoy time spent together” |
| Image | jpg/jpeg | Yes | The image itself | n/a |

# FIGURES
Within the figures folder are some graphical demonstrations of how the models we are using for our image generation work [1]. These explain how an LSTM model works, how a Deep Convoluational Neural Network works, and then how our overall model works for caption generation for each image.

# REFERENCES

[1] D. Team, “Python based project - learn to build Image Caption Generator with CNN & LSTM,” DataFlair, https://data-flair.training/blogs/python-based-project-image-caption-generator-cnn/ (accessed Oct. 8, 2023).\
[2] O. Russakovsky and J. Deng, “Imagenet Large Scale Visual Recognition Challenge 2015 (ILSVRC2015),” ImageNet, https://image-net.org/challenges/LSVRC/2015/2015-downloads.php (accessed Oct. 15, 2023). \
[3] P. Young, A. Lai, M. Hodosh, and J. Hockenmaier, “From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions,” Transactions of the Association for Computational Linguistics, vol. 2, pp. 67–78, 2014. doi:10.1162/tacl_a_00166\
[4] S. A. Khan, “How to change the contrast and brightness of an image using opencv in python?,” How to change the contrast and brightness of an image using OpenCV in Python?, https://www.tutorialspoint.com/how-to-change-the-contrast-and-brightness-of-an-image-using-opencv-in-python (accessed Oct. 15, 2023). \
[5] A. Akbarinia and R. Gil-Rodriguez, “Deciphering image contrast in object classification Deep Networks,” Vision Research, https://www.sciencedirect.com/science/article/pii/S0042698920300766 (accessed Oct. 8, 2023). \
[6] S. Xiang, “How machine learning can help visually impaired people,” Medium, https://towardsdatascience.com/how-can-machine-learning-help-visually-impaired-people-4fcdc76816b2 (accessed Oct. 8, 2023). \
[7] J. Wang, S. Wang, and Y. Zhang, “Artificial Intelligence for Visually impaired,” Displays, https://www.sciencedirect.com/science/article/pii/S0141938223000240 (accessed Oct. 8, 2023). \
[8]</a> [Milestone 1 Document](https://docs.google.com/document/d/1G4Jvo4EQYtKPvtVvIoT4pRWm-4h2_MVep81_-D6IHkw/edit?usp=sharing) \
[9]</a> [Milestone 2 Document](https://docs.google.com/document/d/1dHzD3yrBs_sJ41vBBawssA2my8qmjBXLX12vXCZNdr4/edit?usp=sharing)
