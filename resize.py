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
            # test Extract Variable refactor by highlighting contents of the variable below and choose Extract Variable fom the quick fix
            newImgPath = newResizedFolder + "/resized" + filename
            cv2.imwrite(newImgPath, newImage)
    complete = "Your images have been resized"
    # write code to print the variable above and check for intellisense recommendations
    # once you write the line ensure the linter warning regarding the unused variable goes away


if __name__ == "__main__":
    main()
