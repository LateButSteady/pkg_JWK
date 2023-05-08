#! usr/bin/env python
#!-*- encoding: utf-8 -*-

import fast_glcm
from skimage import data

if __name__ == '__main__':
    img = data.camera()
    glcm_mean = fast_glcm.fast_glcm_mean(img)