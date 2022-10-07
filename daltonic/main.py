import cv2 as cv
import numpy as np

image = cv.imread("roses.jpeg")
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

light_blue = np.array([110,50,50])
dark_blue = np.array([130,255,255])

light_green = np.array([36,25,25])
dark_green = np.array([86, 255,255])

light_red = np.array([0,50,50])
dark_red = np.array([10,255,255])



mask_blue = cv.inRange(hsv, light_blue, dark_blue)
mask_green = cv.inRange(hsv, light_green, dark_green)
mask_red = cv.inRange(hsv, light_red, dark_red)

output_blue = cv.bitwise_and(image,image, mask= mask_blue)
output_green = cv.bitwise_and(image,image, mask= mask_green)
output_red = cv.bitwise_and(image,image, mask= mask_red)

cv.putText(output_blue,"Blue",(170,260),cv.FONT_HERSHEY_SIMPLEX,3,(255,0,0),2,cv.LINE_AA)
cv.putText(output_green,"Green",(170,260),cv.FONT_HERSHEY_SIMPLEX,3,(0,255,0),2,cv.LINE_AA)
cv.putText(output_red,"Red",(170,260),cv.FONT_HERSHEY_SIMPLEX,3,(0,0,255),2,cv.LINE_AA)

cv.imshow("Color Detected", np.hstack((image,output_blue,output_green,output_red)))
cv.waitKey(0)
cv.destroyAllWindows()