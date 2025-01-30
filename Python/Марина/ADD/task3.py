import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

image_path = "C://Users//tiko1//Documents//GitHub//HOMEWORK//Python//ADD//Dogs_love.jpg"
image = mpimg.imread(image_path)

# Проверка: Если изображение в формате uint8, переводим в диапазон [0, 1]
if image.max() > 1:
    image = image / 255.0

# 1. Удаление зеленого цвета
image_no_green = image.copy()
image_no_green[:, :, 1] = 0

# 2. Изменение яркости
brightness_factor = 0.2
image_with_brightness = np.clip(image + brightness_factor, 0, 1)

# 3. Перевод в чёрно-белый формат
image_grayscale = np.dot(image[:, :, :3], [0.2989, 0.587, 0.114])

# 4. Гистограмма зеленого цвета
green_channel = image[:, :, 1]
hist_green, bins = np.histogram(green_channel, bins=256, range=(0, 1))

# 5. Сжатие изображения с использованием SVD
svd_rank = 10
compressed_channels = []
for i in range(3): 
    U, S, Vt = np.linalg.svd(image[:, :, i], full_matrices=False)
    S[svd_rank:] = 0
    compressed_channel = np.dot(U, np.dot(np.diag(S), Vt))
    compressed_channels.append(compressed_channel)

image_compressed = np.stack(compressed_channels, axis=2)


plt.figure(figsize=(8, 8))
plt.imshow(image)
plt.title("Исходное изображение")
plt.axis("off")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(image_no_green)
plt.title("Без зеленого цвета")
plt.axis("off")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(image_with_brightness)
plt.title("Изменённая яркость")
plt.axis("off")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(image_grayscale, cmap="gray")
plt.title("Чёрно-белое изображение")
plt.axis("off")
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(bins[:-1], hist_green, color="green")
plt.title("Гистограмма зеленого цвета")
plt.xlabel("Интенсивность")
plt.ylabel("Количество пикселей")
plt.show()

plt.figure(figsize=(8, 8))
plt.imshow(image_compressed)
plt.title("Сжатое изображение (SVD)")
plt.axis("off")
plt.show()
