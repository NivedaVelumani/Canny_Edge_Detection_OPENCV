import cv2
img=cv2.imread("lane.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)
cv2.imwrite("gray_image.png",gray)


edge_low=cv2.Canny(gray , 40,150)
cv2.imshow("edge show" , edge_low)
cv2.waitKey(0)
cv2.imwrite("edge_low.png" , edge_low)

edge_mid=cv2.Canny(gray, 70,150)
cv2.imshow("edge show2" , edge_mid)
cv2.waitKey(0)
cv2.imwrite("edge_mid.png" , edge_mid)

edge_high=cv2.Canny(gray , 120,250)
cv2.imshow("edge show3" , edge_high)
cv2.waitKey(0)			
cv2.imwrite("edge_high.jpg" , edge_high)

