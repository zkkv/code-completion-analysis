import cv2
import numpy as np

def get_contours(plate_image, orig):
    canny_image = cv2.Canny(plate_image, 50, 100)
    canny_image = cv2.morphologyEx(canny_image, cv2.MORPH_DILATE, np.ones((2, 2)))
    canny_image = cv2.morphologyEx(canny_image, cv2.MORPH_ERODE, np.ones((2, 2)))

    contours, _ = cv2.findContours(canny_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnts = sorted(contours, key=lambda x: cv2.arcLength(x, True), reverse=True)[:30]

    if len(cnts) == 0:
        return None

    return cnts[0]


def create_sift_descriptor(image):
    if len(image.shape) == 3:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        img = image
    sift = cv2.SIFT_create()

    _, descriptors = sift.detectAndCompute(img, None)
    return descriptors