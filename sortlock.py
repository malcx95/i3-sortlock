import numpy as np
import matplotlib.colors as colors
import imageio
import random

BLOCK_SIZE = 10

# 0 for hue
# 1 for saturation
# 2 for value
SORTMETHOD = 1


def get_block_list(img, height, width):
    res = []
    for y in range(height):
        for x in range(width):
            res.append(img[y*BLOCK_SIZE:(y + 1)*BLOCK_SIZE,
                           x*BLOCK_SIZE:(x + 1)*BLOCK_SIZE, :])
    return res


def block_list_to_img(block_list, height, width, sh, sw):
    img = np.empty((sh, sw, 3))
    for x in range(width):
        for y in range(height):
            block = block_list[y*width + x][1]
            img[y*BLOCK_SIZE:(y + 1)*BLOCK_SIZE, x*BLOCK_SIZE:(x + 1)*BLOCK_SIZE, :] = block
    return img


def magnitude(block):
    hsv_block = colors.rgb_to_hsv(block)
    return np.sum(hsv_block[:, :, SORTMETHOD])


def main():
    img = np.array(imageio.imread("/tmp/screen.png"))
    h, w, _ = img.shape
    width = w // BLOCK_SIZE
    height = h // BLOCK_SIZE
    block_list = get_block_list(img, height, width)
    random.shuffle(block_list)
    magnitudes = list(map(lambda b: (magnitude(b), b), block_list))
    magnitudes.sort(key=lambda m: m[0])
    new_img = block_list_to_img(magnitudes, height, width, h, w)
    imageio.imwrite("/tmp/screen.png", new_img)


if __name__ == "__main__":
    main()

