from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse
import os
import csv
import re


# ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--image', required=True, help="Image Path")
# args = vars(ap.parse_args())
# img_path = args['image']

# img_path = "DATA/well_lit_test_set/ILSVRC2015_test_00000015.JPEG"

def extract_features(filename, model):
        try:
            image = Image.open(filename)

        except:
            print("ERROR: Couldn't open image! Make sure the image path and extension is correct")
        image = image.resize((299,299))
        image = np.array(image)
        # for images that has 4 channels, we convert them into 3 channels
        if len(image.shape) == 2:
            image = np.stack([image]*3, axis=-1)
        if image.shape[2] == 4: 
            image = image[..., :3]
        image = np.expand_dims(image, axis=0)
        image = image/127.5
        image = image - 1.0
        feature = model.predict(image)
        return feature

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None


def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([photo,sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text


def save_test_results(test_dataset, csv_path):
    # well_lit_test = os.listdir("DATA/well_lit_test_set")
    # print(well_lit_test)
    output_csv_path = f"DATA/{csv_path}"
    if not os.path.exists(output_csv_path):
        test_dataset_images = os.listdir(f"DATA/{test_dataset}")

        with open(output_csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for test_img in test_dataset_images:
                img_path = f"DATA/{test_dataset}/{test_img}"
                print(img_path)

                # CHANGE max_length to what expected shape size should be in the ValueError if there is an error
                max_length = 32

                tokenizer = load(open("tokenizer.p","rb"))
                model = load_model('models/model_9.h5') #file path may need to be changed if we put model in a different path
                xception_model = Xception(include_top=False, pooling="avg")

                photo = extract_features(img_path, xception_model)
                img = Image.open(img_path)

                description = generate_desc(model, tokenizer, photo, max_length)
                print("\n\n")
                # print(description)
                filtered_description = re.sub(r'^start\s+|\s+end$', '', description)
                print(filtered_description)
                csv_writer.writerow([test_img, filtered_description])
                plt.imshow(img)

save_test_results("well_lit_test_set", "well_lit_results.csv")

save_test_results("black_and_white_test_set", "black_white_results.csv")

save_test_results("low_contrast_test_set", "low_contrast_results.csv")

