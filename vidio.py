import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('result')


while True:
    ret, frame = cap.read()
    frame_copy = frame.copy()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    frame_h = frame_hsv[:, :, 0]
    frame_s = frame_hsv[:, :, 1]
    frame_v = frame_hsv[:, :, 2]
#КРАСНЫЙ
    min_ = (0,130,40)
    max_ = (21,160,170)

    min1_ = (155,135,40)
    max1_ = (180,155,180)

    mask = cv2.inRange(frame_hsv, min_, max_)
    mask2 = cv2.inRange(frame_hsv, min1_, max1_)
    result2 = cv2.bitwise_or(mask2, mask)
    result = cv2.bitwise_and(frame, frame, mask=result2)
    # Ищем контуры
    contours = cv2.findContours(result2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # Сами структуры контуров хранятся в начальном элементе возвращаемого значения:
    contours = contours[0]

    # Их, кстати, может и не быть:
    if contours:

        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        # Третий аргумент — это индекс контура, который мы хотим вывести. Мы хотим самый большой.
        # Вывести все можно, передав -1 вместо 0:
        cv2.drawContours(result, contours, 0, (255, 0, 0), 1)

        # Получаем прямоугольник, обрамляющий наш контур:
        (x, y, w, h) = cv2.boundingRect(contours[0])

        # И выводим его:
        cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 1)

        # Аналогично строим минимальную описанную вокруг наибольшего контура окружность:
        (x1, y1), radius = cv2.minEnclosingCircle(contours[0])
        center = (int(x1), int(y1))
        radius = int(radius)
        cv2.circle(result, center, radius, (0, 255, 0), 1)
        cv2.line(, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)
    cv2.imshow('mask', result2)
    cv2.imshow('result', result)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()