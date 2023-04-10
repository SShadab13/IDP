import cv2 as cv

img = cv.imread("testImages/testIMG01.png")

cv.imshow("IMG", img)


# converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

##






cv.waitKey(0)



