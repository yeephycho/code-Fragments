#! /usr/bin/env python

# This file define python script to get image properities.

import cv2
import os

def crop_center_square(image):
    if(2 == image.ndim):
        height, width = image.shape
    elif(3 == image.ndim):
        height, width, channel = image.shape
    else:
        print("Image dimension should be 2 or 3")

    if (height >= width):
        radius = width/2
        center_height = height/2
        center_width = width/2
        start_height = center_height - radius
        crop_image = image[start_height:(start_height + 2 * radius), 0:(2 * radius)]
        return crop_image
    else:
        radius = height/2
        center_height = height/2
        center_width = width/2
        start_width = center_width - radius
        crop_image = image[0:(2 * radius), start_width:(start_width + 2 * radius)]
        return crop_image

def crop_square(image, percentage):
    if (2 == image.ndim):
        height, width = image.shape
    elif (3 == image.ndim):
        height, width, channel = image.shape
    else:
        print("Image dimension should be 2 or 3")
    if (height >= width):
        radius = width/2
        center_height = height/2
        center_width = width/2
        minimum_center_height = radius
        maximum_center_height = height - radius
        center_height_scope = maximum_center_height - minimum_center_height
        start_height = minimum_center_height + (center_height_scope * percentage/100) - radius
        crop_image = image[start_height:(start_height + 2 * radius), 0:(2 * radius)]
        return crop_image
    else:
        radius = height/2
        center_height = height/2
        center_widht = width/2
        minimum_center_width = radius
        maximum_center_width = width - radius
        center_width_scope = maximum_center_width - minimum_center_width
        start_width = minimum_center_width + (center_width_scope * percentage/100) - radius
        crop_image = image[0:(2*radius), start_width:(start_width + 2 * radius)]
        return crop_image

image = cv2.imread("./test_image/lennon-1.jpg")
print image.shape
#crop_image = crop_center_square(image)
crop_image = crop_square(image, 100)
print crop_image.shape

try:
    os.stat("./test_image/output/")
except:
    os.mkdir("./test_image/output/")

cv2.imwrite("./test_image/output/square.jpg", crop_image)
rsz_image = cv2.resize(crop_image, (256, 256))
print rsz_image.shape
cv2.imwrite("./test_image/output/rsz_image.jpg", rsz_image)

rsz_image2 = cv2.resize(crop_image, (20, 20))
cv2.imwrite("./test_image/output/small_image.jpg", rsz_image2)
