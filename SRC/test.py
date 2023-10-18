filename = "../DATA/flicker30k-captions.txt"

def load_doc(filename):
    # Opening the file as read only
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


def all_img_captions(filename):
    file = load_doc(filename)
    captions = file.split('\n')
    descriptions ={}
    trainfile = open("../DATA/Flickr_30k.trainImages.txt", 'w')
    for caption in captions[:-1]:
        #print(caption)
        img, caption = caption.split(', ', 1)
        if img not in descriptions:
            descriptions[img] = [ caption ]
            trainfile.write(img + "\n")
        else:
            descriptions[img].append(caption)
    return descriptions

dictionary = all_img_captions(filename)
