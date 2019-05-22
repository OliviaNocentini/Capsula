#!/usr/bin/env python3
# Detection and removal based on study [1].
# Note that notations (r_, m_, s_) are adapted from the paper.
import cv2
import numpy as np
import specularity as spc  

impath = 'figs/original.png'
img = cv2.imread(impath)
gray_img = spc.derive_graym(impath)

r_img = m_img = np.array(gray_img)

rimg = spc.derive_m(img, r_img)
s_img = spc.derive_saturation(img, rimg)
spec_mask = spc.check_pixel_specularity(rimg, s_img)
enlarged_spec = spc.enlarge_specularity(spec_mask)
    
# use opencv's inpaint methods to remove specularity
radius = 12 
telea = cv2.inpaint(img, enlarged_spec, radius, cv2.INPAINT_TELEA)
ns = cv2.inpaint(img, enlarged_spec, radius, cv2.INPAINT_NS)

cv2.imwrite('figs/Impainted_telea.png',telea)
cv2.imwrite('figs/Impainted_ns.png',ns)

cv2.imshow('figs/original.png',img)
cv2.waitKey(0)

cv2.imshow('figs/Impainted_telea.png',telea)
cv2.waitKey(0)


cv2.imshow('figs/Impainted_ns.png',ns)
cv2.waitKey(0)



