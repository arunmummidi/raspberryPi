# Import libraries
import cv2
import numpy
import matplotlib.pyplot as pyplot

image = cv2.imread('/home/arunodaya/count.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
pyplot.imshow(gray, cmap='gray')

#cv2.imshow("Image with gray", image)
cv2.imshow(gray, cmap='gray', image)
cv2.waitKey(0)

blur = cv2.GaussianBlur(gray, (11, 11), 0)
pyplot.imshow(blur, cmap='gray')

canny = cv2.Canny(blur, 30, 150, 3)
pyplot.imshow(canny, cmap='gray')

dilated = cv2.dilate(canny, (1, 1), iterations=0)
pyplot.imshow(dilated, cmap='gray')


(cnt, hierarchy) = cv2.findContours(
	dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

pyplot.imshow(rgb)

print("coins in the image : ", len(cnt))

