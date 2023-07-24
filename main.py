import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    frame = cv2.medianBlur(frame, 7)
    # converting image into grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    # threshold = cv2.adaptiveThreshold(
    #    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # using a findContours() function
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area, largest to smallest, and filter out small areas

    largest_contours = contours = sorted(contours, key=lambda x: cv2.contourArea(
        x), reverse=True)
    for i in range(len(largest_contours)):
        if cv2.contourArea(largest_contours[i]) <= 15:
            largest_contours = largest_contours[1:i]
            break

    i = 0

    # for contour in contours:
    for contour in largest_contours:
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.02 * cv2.arcLength(contour, True), True)

        # using drawContours() function
        cv2.drawContours(frame, [contour], 0, (0, 0, 255), 3)

        # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

            # putting shape name at center of each shape
            cv2.putText(frame, str(len(approx)), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

vid.release()
cv2.destroyAllWindows()
