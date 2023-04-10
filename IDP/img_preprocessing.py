#%%
# Importing all the Libraries and packages
import cv2 as cv
import numpy as np
import PIL

# %%
img = cv.imread("testImages/testIMG01.png")

cv.imshow("IMG", img)

cv.waitKey(0)
cv.destroyAllWindows()


# %%
# Normalization

normalized_img = cv.normalize(img, None, 0, 255, cv.NORM_MINMAX)


cv.imshow("Normalized Img", normalized_img)
cv.waitKey(0)
cv.destroyAllWindows()


# %%
# Image Scaling
length_x, width_y = img.shape[:2]

print(length_x)
print(width_y)




# %%
factor = min(1, float(1024.0/ length_x))

# %%
print(factor)
# %%
