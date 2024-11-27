import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Загрузка изображения
image_path = "C://Users//tiko1//Documents//GitHub//HOMEWORK//Python//ADD_3_V2_Herashchenko//image.jpg"
image = mpimg.imread(image_path)

# Проверка: Если изображение в формате uint8, переводим в диапазон [0, 1]
if image.max() > 1:
    image = image / 255.0

# 1. Удаление синего цвета
image_no_blue = image.copy()
image_no_blue[:, :, 2] = 0  # Установка синего канала в 0

# 2. Изменение яркости
brightness_factor = 0.2  # Яркость: прибавим к пикселям
image_bright = np.clip(image + brightness_factor, 0, 1)  # Убедимся, что значения остаются в диапазоне [0, 1]

# 3. Перевод в чёрно-белый формат
image_gray = np.dot(image[..., :3], [0.2989, 0.587, 0.114])  # Формула для перевода в grayscale

# 4. Гистограмма синего цвета
blue_channel = image[:, :, 2]
hist_blue, bins = np.histogram(blue_channel, bins=256, range=(0, 1))

# 5. Сжатие изображения с использованием SVD
def svd_compression(image_channel, num_singular_values):
    U, S, Vt = np.linalg.svd(image_channel, full_matrices=False)
    S[num_singular_values:] = 0
    return np.dot(U, np.dot(np.diag(S), Vt))

# Сжатие каждого цветового канала
svd_rank = 50
compressed_channels = [svd_compression(image[:, :, i], svd_rank) for i in range(3)]
image_compressed = np.stack(compressed_channels, axis=2)

# Отображение результатов
def show_image(image, title, cmap=None):
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()

# Исходное изображение
show_image(image, "Исходное изображение")

# Без синего цвета
show_image(image_no_blue, "Без синего цвета")

# Изменённая яркость
show_image(image_bright, "Изменённая яркость")

# Чёрно-белое изображение
show_image(image_gray, "Чёрно-белое изображение", cmap="gray")

# Гистограмма синего цвета
plt.figure(figsize=(8, 8))
plt.plot(bins[:-1], hist_blue, color="blue")
plt.title("Гистограмма синего цвета")
plt.xlabel("Интенсивность")
plt.ylabel("Количество пикселей")
plt.show()

# Сжатое изображение
show_image(image_compressed, "Сжатое изображение (SVD)")
