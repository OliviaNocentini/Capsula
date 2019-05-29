#!/usr/bin/env python3
import cv2
import numpy as np

# import image
image = cv2.imread('/home/centauro/test/ciao.jpg')
cv2.imshow("normal", image)
cv2.waitKey(0)
cropped = image[800:1080, 400:1080]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)

# grayscale
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# binary
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('threshold', thresh)

# dilation
kernel = np.ones((10, 1), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated', img_dilation)

# find contours
im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    print(h)
    print(w)
    print(x)
    print(y)

    cx= int(x+w/2)
    print(cx)
    cy= int(y+h/2)
    print(cy)



	
	 # Getting ROI
    roi = cropped[y:y + h, x:x + w]

    # show ROI
    # cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(cropped, (x, y), (x + w, y + h), (0, 255, 0), 2)



    if w > 15 and h > 15:
        cv2.imwrite('C:\\Users\\PC\\Desktop\\output\\{}.png'.format(i), roi)

        cv2.circle(cropped, (cx,cy),3, (0, 0, 255), -1)

cv2.imshow('marked areas', cropped)
cv2.waitKey(0)