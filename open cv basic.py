# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
img=cv2.imread("download.jpg",1)
print(img)

print(img.shape)

resized_img=cv2.resize(img,(600,600))
cv2.imshow("yeshhh",resized_img)
cv2.imshow("yesh",img)
cv2.waitKey()
cv2.destroyAllWindows()