### Scaling, Rotation and Translation an image ###

# import needed libraries
import cv2
import numpy as numpy

FILE_NAME = 'image.png'

### Scaling ####
window_name = 'Scaling Image'

img  = cv2.imread(FILE_NAME)
(height, width) = img.shape[:2]
res = cv2.resize(img, (int(width / 2), int (height/2)),
                    interpolation = cv2.INTER_CUBIC)

cv2.imshow("source", img)
cv2.imshow(window_name, res)
cv2.waitKey(0)

### Rotation ####
window_name = 'Rotation Image'

img = cv2.imread(FILE_NAME)
res = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow(window_name, res)
cv2.waitKey(0)

#### Cut image ####
window_name = "Cropped image"

img = cv2.imread(FILE_NAME)
print(img.shape)

cropped_image = img[0:75, 0:75]

cv2.imshow("Original", img)
cv2.imshow("Cropped", cropped_image)
cv2.waitKey(0)
