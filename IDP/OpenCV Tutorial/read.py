#%%
import cv2 as cv

img = cv.imread("Codes/OpenCV Tutorial/testImages/testIMG01.png")


#%%
## REading the Cat image
img_cat = cv.imread("testImages/Photos/cat.jpg")
cv.imshow("Cat", img_cat)
cv.waitKey(0)
cv.destroyAllWindows()


#%%
## Reading a Video
capture = cv.videoCapture("testImages/Videos/dog.mp4")

# Reading the video frame by frame
while True:
    isTrue, frame= capture.read()

