import cv2
import numpy as np

# Đọc ảnh đầu vào
image = cv2.imread('imgs/geometry.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Phát hiện các đường tròn trong ảnh
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=100)

# Nếu có đường tròn được phát hiện
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    
    # Vẽ các đường tròn được phát hiện
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 0), 3)

    # Hiển thị ảnh kết quả
    cv2.imshow("Detected Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Không tìm thấy đường tròn trong ảnh.")
