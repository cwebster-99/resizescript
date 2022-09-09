import os

import cv2


def resizeImg(image, width=None, height=None):

    scale_percent = 60 
    
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return resized

def main():
    folder = "./originalImgs"
    newResizedFolder = "./newResizedImgs"

    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            newImage = resizeImg(img)
            newImgPath = newResizedFolder + '/resized' + filename
            cv2.imwrite(newImgPath, newImage)


if __name__ == "__main__":
    main()




