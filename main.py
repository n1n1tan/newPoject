import cv2
import os
img = cv2.imread('./data/road-signs/approaching-a-pedestrian-crossing.jpg')
img1 = cv2.imread('./data/road-signs/footpath.jpg')
img2 = cv2.imread('./data/road-signs/left-turn.jpg')
img3 = cv2.imread('./data/road-signs/mechanical-transport-prohibition.jpg')
img4 = cv2.imread('./data/road-signs/movement-prohibition.jpg')
img5 = cv2.imread('./data/road-signs/no-entry.jpg')
img6 = cv2.imread('./data/road-signs/no-overtaking.jpg')
img7 = cv2.imread('./data/road-signs/roundabout.jpg')

if img is None:
    print('Файл не найден')
    os._exit(1)
#
# img.itemset((10,10,0), 0)
# img.itemset((11,11,1), 0)
# img.itemset((9,9,2), 0)




# print(img.shape)
# print(img.size)
# print(img.dtype)

# x_max, y_max, _ = img.shape
# x = x_max // 2
# y = y_max // 2
# print(img.item(x, y, 0))
# new = (img.item(x, y, 0), img.item(x, y, 1), img.item(x, y, 2))


x,x_max,y,y_max = map(int, input("введи координаты:").split())
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', img[x:x_max, y:y_max])
while True:
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyWindow()
