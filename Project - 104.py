import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "< Sun", (60, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0))

cv2.putText(img, "Mercury", (110, 240), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Venus", (190, 170), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Earth", (290, 260), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Mars", (385, 170), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Jupiter", (550, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Saturn", (780, 130), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Uranus", (970, 140), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))

cv2.putText(img, "Neptune", (1110, 140), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 255, 0))


cv2.imshow("First time using cv2. Pardon me for any stupidness", img)
cv2.waitKey(0)