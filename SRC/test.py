filename = "../DATA/Flickr_30k.trainImages.txt"

def load_doc(filename):
    # Opening the file as read only
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


def all_img_captions(filename):
    file = load_doc(filename)
    captions = file.split('\n')

    new_captions_file = open("../DATA/flickr30k-random-contrast-trainImages.txt", "w")

    for caption in captions[:-1]:
        name, extension = caption.split(".")
        name = name + "_random_contrast"
        extension = "jpeg"
        new_filename = name + "." + extension

        new_captions_file.write(new_filename + "\n")
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
