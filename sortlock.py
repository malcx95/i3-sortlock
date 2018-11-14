import numpy as np
import matplotlib.colors as colors
import scipy.ndimage as im
import scipy.misc as imw

BLOCK_SIZE = 50

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
            block = block_list[y*width + x]
            img[y*BLOCK_SIZE:(y + 1)*BLOCK_SIZE, x*BLOCK_SIZE:(x + 1)*BLOCK_SIZE, :] = block
    return img


def magnitude(block):
    hsv_block = colors.rgb_to_hsv(block)
    return np.sum(hsv_block[:, :, SORTMETHOD])


def main():
    img = np.array(im.imread("/tmp/screen.png"))
    h, w, _ = img.shape
    width = w // BLOCK_SIZE
    height = h // BLOCK_SIZE
    block_list = get_block_list(img, height, width)
    block_list.sort(key=magnitude)
    new_img = block_list_to_img(block_list, height, width, h, w)
    imw.imsave("/tmp/screen.png", new_img)



if __name__ == "__main__":
    main()

