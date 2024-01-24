import os
import cv2


def loadGrey(filename):
    path = os.path.join(os.getcwd(), 'images', filename)
    image = cv2.imread(path)
    greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return greyscale


def getDoG(greyscale):
    # apply gaussian filter
    gausImg = cv2.GaussianBlur(greyscale, (13, 13), 7)

    #denoise
    medianImg = cv2.medianBlur(gausImg, 5)
    result = cv2.adaptiveThreshold(medianImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 7)

    result = result - greyscale

    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result

