# DS Project Course Project 2

## Repository Contents

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

### Code usage
In order to run our code, use the command ```python3 SRC/testing_generator.py``` This will output the test results for the images from the well lit, black and white, and low contrast datasets in the well_lit_results.csv, black_white_results.csv, and low_contrast_results.csv respectively with each image from the dataset and its generated caption in the same line. In order to generate ca


# DATA
Within our data folder, there are three subfolders which contain our three test sets. Each subfolder contains 100 images that can be used by `testing_generator.py` to create captions for analysis of the model. `flicker30k-captions.txt` contains the set of image names with each of their 5 corresponding captions which is used in training the model. `Flickr_30k.trainImages.txt` is a newline separated list of each of the image names inthe flickr30k dataset which is needed for training the model. The main Flikr30k images dataset and the random contrast version of the set do not fit on github due to their size, so they can be accessed from our google drive data folder [here](https://drive.google.com/drive/folders/1ye6XsPeA9_LKVxbcmmriqXtG1ADnkz-F?usp=sharing). The two image files on the google drive are named `flickr30k-images.tar.gz` and `flickr30k-random-contrastimages.zip`. Both of these image sets contain the same 30,000 images. The random contrast dataset has modified the original flikr30k set to have random contrast on the images. The code for this change can be seen in `create_random_contrast_train_set.py`.

# FIGURES

# REFERENCES

[1] D. Team, “Python based project - learn to build Image Caption Generator with CNN & LSTM,” DataFlair, https://data-flair.training/blogs/python-based-project-image-caption-generator-cnn/ (accessed Oct. 8, 2023).
[2] O. Russakovsky and J. Deng, “Imagenet Large Scale Visual Recognition Challenge 2015 (ILSVRC2015),” ImageNet, https://image-net.org/challenges/LSVRC/2015/2015-downloads.php (accessed Oct. 15, 2023). 
[3] P. Young, A. Lai, M. Hodosh, and J. Hockenmaier, “From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions,” Transactions of the Association for Computational Linguistics, vol. 2, pp. 67–78, 2014. doi:10.1162/tacl_a_00166
[4] S. A. Khan, “How to change the contrast and brightness of an image using opencv in python?,” How to change the contrast and brightness of an image using OpenCV in Python?, https://www.tutorialspoint.com/how-to-change-the-contrast-and-brightness-of-an-image-using-opencv-in-python (accessed Oct. 15, 2023). 
[5] A. Akbarinia and R. Gil-Rodriguez, “Deciphering image contrast in object classification Deep Networks,” Vision Research, https://www.sciencedirect.com/science/article/pii/S0042698920300766 (accessed Oct. 8, 2023). 
[6] S. Xiang, “How machine learning can help visually impaired people,” Medium, https://towardsdatascience.com/how-can-machine-learning-help-visually-impaired-people-4fcdc76816b2 (accessed Oct. 8, 2023). 
[7] J. Wang, S. Wang, and Y. Zhang, “Artificial Intelligence for Visually impaired,” Displays, https://www.sciencedirect.com/science/article/pii/S0141938223000240 (accessed Oct. 8, 2023). 
