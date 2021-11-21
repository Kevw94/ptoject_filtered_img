import cv2
import numpy as np
import os
from os.path import basename


image_path = 'Data/images/img_test.png'




class AllFilters():
    global image_path

    def gray_filter(self):
        self.read = cv2.imread(image_path)
        self.gray = cv2.cvtColor(self.read, cv2.COLOR_BGR2GRAY)
        os.chdir('output')
        cv2.imwrite(basename(image_path), self.gray)

    def blur_filter(self):
        self.read = cv2.imread(image_path)
        self.blur = cv2.GaussianBlur(self.read, (41, 41), cv2.BORDER_DEFAULT)
        os.chdir('output')
        cv2.imwrite(basename(image_path), self.blur)

    def dilate_filter(self):
        self.read = cv2.imread(image_path)
        self.kernel = np.ones((61, 61), np.uint8)
        self.dilate = cv2.dilate(self.read, self.kernel, iterations=1)
        os.chdir('output')
        cv2.imwrite(basename(image_path), self.dilate)



#-------------------- test --------------------------------------------
# image_read = cv2.imread(image_path)


# image_gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
# image_blur = cv2.GaussianBlur(image_gray, (41, 41), cv2.BORDER_DEFAULT)
# kernel = np.ones((61, 61), np.uint8)
# image_dilate = cv2.dilate(image_blur, kernel, iterations=1)
# changeDir = os.chdir('output')
# cv2.imwrite(basename(image_path), image_dilate)





# class GrayFilter():
#     read = cv2.imread(image_path)

#     def __init__(self):  # image_path
#         self.gray = cv2.cvtColor(self.read, cv2.COLOR_BGR2GRAY)
#         os.chdir('output')
#         cv2.imwrite(basename(image_path), self.gray)


# class BlurFilter():

#     def __init__(self):
#         self.read = cv2.imread(image_path)
#         self.blur = cv2.GaussianBlur(self.read, (41, 41), cv2.BORDER_DEFAULT)
#         os.chdir('output')
#         cv2.imwrite(basename(image_path), self.blur)


# class DilateFilter():

#     def __init__(self):
#         self.read = cv2.imread(image_path)
#         self.kernel = np.ones((61, 61), np.uint8)
#         self.dilate = cv2.dilate(self.read, self.kernel, iterations=1)
#         os.chdir('output')
#         cv2.imwrite(basename(image_path), self.dilate)
