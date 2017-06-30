#! /usr/bin/env python

import numpy as np
import cv2

image = cv2.imread("./cat.jpg")

def get_image_info(image):
    print(image.shape)
    print(image.dtype)

def image_reshape(image, shape):
    image_reshape = image.reshape(shape)
    return image_reshape

def WHC2CWH(image):
    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 2]
    image_cwh = np.array([r, g, b])
    return image_cwh

def bgr2rgb(image):
    image_rgb = image[:, :, ::-1]
    return image_rgb

