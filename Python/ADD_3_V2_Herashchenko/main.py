import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

image_path = "C:\\ALL\\GitHub repositories\\HOMEWORK\\Python\\ADD_3_V2_Herashchenko\\image.jpg"
image = mpimg.imread(image_path)

if image.max() > 1:
    image = image / 255.0

image_no_blue = image.copy()
image_no_blue[:, :, 2] = 0

brightness_factor = 0.2
image_bright = np.clip(image + brightness_factor, 0, 1)

image_gray = np.dot(image[..., :3], [0.2989, 0.587, 0.114])

blue_channel = image[:, :, 2]
hist_blue, bins = np.histogram(blue_channel, bins=256, range=(0, 1))

def svd_compression(image_channel, num_singular_values):
    U, S, Vt = np.linalg.svd(image_channel, full_matrices=False)
    S[num_singular_values:] = 0
    return np.dot(U, np.dot(np.diag(S), Vt))

svd_rank = 10
compressed_channels = [svd_compression(image[:, :, i], svd_rank) for i in range(3)]
image_compressed = np.stack(compressed_channels, axis=2)

def show_image(image, title, cmap=None):
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()

show_image(image, "Исходное изображение")

show_image(image_no_blue, "Без синего цвета")

show_image(image_bright, "Изменённая яркость")

show_image(image_gray, "Чёрно-белое изображение", cmap="gray")

plt.figure(figsize=(8, 8))
plt.plot(bins[:-1], hist_blue, color="blue")
plt.title("Гистограмма синего цвета")
plt.xlabel("Интенсивность")
plt.ylabel("Количество пикселей")
plt.show()

show_image(image_compressed, "Сжатое изображение (SVD)")