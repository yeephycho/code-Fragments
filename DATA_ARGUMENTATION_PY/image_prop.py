#!/usr/bin/env python

# This file define python script to get image properities.

import cv2

def get_dim(image):
    return image.ndim

def get_shape_2d(image):
    return height, width = image.shape

def get_shape_3d(image):
    return height, width, channel = image.shape

def crop_image_square(image):
    if(2 == get_dim(image)):
        height, width = get_shape_2d(image)
    elif(3 == get_dim(image)):
        height, width, channel = get_shape_3d(image)
    else
        print("Image dimension should be 2 or 3")

    if (height >= width):
        if_vertial = True
        radius = width/2
        center_height = height/2
        center_width = width/2
        start_height = center_height - radius
        crop_image = image[start_height:(start_height + 2 * radius), 0:(2 * radius)]
        return crop_image
    else
        if_vertial = False
        radius = height/2
        center_height = height/2
        center_width = width/2
        start_width = center_width - radius
        crop_image = image[0:(2 * radius), start_width:(start_width + 2 * radius)]
        return crop_image


