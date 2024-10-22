import numpy as np
import cv2

# Создаем массив 1x1 с значением 0 (черный цвет)
black_pixel = np.array([[0]], dtype=np.uint8)

# Сохраняем черный пиксель как изображение
cv2.imwrite('color_image.jpg', black_pixel)

# Создаем массив 1x1 с значением 255 (белый цвет)
white_pixel = np.array([[255]], dtype=np.uint8)

# Сохраняем белый пиксель как изображение
cv2.imwrite('color_image.jpg', white_pixel)
