import cv2
import numpy as np
import os
import random
import argparse
IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def split(dir):
    root = sorted(os.walk(dir))
    
    if not os.path.exists('folder1/'):
            os.makedirs('folder1/')
    if not os.path.exists('folder2/'):
            os.makedirs('folder2/')
    if not os.path.exists('folder3/'):
            os.makedirs('folder3/')
    for i in range(len(root[0][2])):
        img = random.choice(root[0][2])
        print(img)
        if is_image_file(img):
            image = cv2.imread(dir+img,1)
            if i%3==1:
                cv2.imwrite('folder1/'+img,image)
            elif i%3==2:
                cv2.imwrite('folder2/'+img,image)
            else:
                cv2.imwrite('folder3/'+img,image)
            os.remove(dir+img)
            root = sorted(os.walk(dir))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = True,
    help = "path to where the images resides")
    args = vars(ap.parse_args())
    split(args["path"])
