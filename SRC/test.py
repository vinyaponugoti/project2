filename = "../DATA/low_contrast_random_contrast_results.csv"

def load_doc(filename):
    # Opening the file as read only
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


def all_img_captions(filename):
    file = load_doc(filename)
    captions = file.split('\n')

    test_results = open("../DATA/low_contrast_random_contrast_accuracy.txt", "w")

    overall_accuracy_count = 0

    for caption in captions[:-1]:
        filename, caption = caption.split(",", 1)
        print("filename:", filename)
        print("caption:", caption)
        accuracy = input("accuracy score: ")
        overall_accuracy_count += accuracy

        test_results.write(filename + "," + str(accuracy))

    test_results.write("\n\noverall accuracy: " + str(overall_accuracy_count) + "%")
    # descriptions ={}
    # trainfile = open("../DATA/Flickr_30k.trainImages.txt", 'w')
    # for caption in captions[:-1]:
    #     print(caption)
    #     img, caption = caption.split(', ', 1)
    #     if img not in descriptions:
    #         descriptions[img] = [ caption ]
    #         trainfile.write(img + "\n")
    #     else:
    #         descriptions[img].append(caption)
    # return descriptions

all_img_captions(filename)
