import cv2 
import numpy as np
import matplotlib.pyplot as plt
import math

im = cv2.cvtColor(cv2.imread('images/230517_154124_0000000025_CAM1_OK.bmp'), cv2.COLOR_BGR2GRAY)
# im.astype('double')
im_crp = im[0:1250,950:1300]
im_inv = 255-im_crp
im_edges = cv2.Canny(im_inv,30,180)
lines_old = cv2.HoughLines(im_edges, 2, np.pi/180, 150, None, 0, 0)
lines = lines_old[0:2]
print(lines)
# Draw lines on the image
if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(im_edges, pt1, pt2, (255,0,0), 1, cv2.LINE_AA)
plt.imshow(im_edges,cmap='gray')
plt.show()
