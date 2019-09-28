import cv2
import numpy as np


def contour_convexity_defects(contour):
    defect_vectors = []
    hull = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull)
    if type(defects) is np.ndarray:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            p1 = tuple(contour[f][0])
            p2 = tuple((contour[s][0] + contour[e][0]) // 2)
            defect_vectors.append((p1, p2))
    return defect_vectors


img = cv2.imread('star2.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
contours, hierarchy = cv2.findContours(thresh,2,1)
cnt = contours[0]

defects = contour_convexity_defects(cnt)
for defect in defects:
    cv2.arrowedLine(img, defect[0], defect[1], [0, 255, 0], 2)
    cv2.circle(img, defect[0], 5, [0, 0, 255], -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
