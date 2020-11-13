from Helping import *


def hist_eq(image: np.ndarray):
    height, width = image.shape
    values, freq = np.unique(image, return_counts=True)
    cum_sum = np.cumsum(freq)
    replace = dict(zip(values, (cum_sum * ((L - 1) / (height * width)))))
    image = np.vectorize(replace.get)(image)
    return image


L = 256
moonOriginal = read_GIF("res/moonOriginal.gif")
toys = read_GIF("res/toys.GIF")
histEqMoon = hist_eq(moonOriginal).astype('uint8')
cv2.imshow('Histogram-equalized moon image', histEqMoon)
cv2.imwrite('out/histogram_equalized_moon_image.png', histEqMoon)
cv2.waitKey()
cv2.destroyWindow('Histogram-equalized moon image')
histEqToys = hist_eq(toys).astype('uint8')
cv2.imshow('Histogram-equalized toys image', histEqToys)
cv2.imwrite('out/histogram_equalized_toys_image.png', histEqToys)
cv2.waitKey()