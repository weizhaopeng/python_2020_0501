from PIL import Image, ImageFilter

def main():
    image = Image.open('../network_t/guido.jpg')
    print(image.format, image.size, image.mode)
    image.show()

    # 进行裁剪
    # 左，上，右，下的边的位置，相比第一个像素的(0, 0)
    # defining the left, upper, right, and lower pixel
    rect = (100, 300, 500, 700)
    # 也就是需要从长100-500， 高300-700,所以是正方形
    # image.crop(rect).show()

    # 生成缩略图，指定了长高进行缩放
    # 函数会保持图片的宽高比例。如果输入的参数宽高和原图像宽高比不同，则会依据最小对应边进行原比例缩放。
    # 所以这里就是以1041:100进行缩放
    size = (685, 100)
    # image.thumbnail(size)
    # image.show()

    # 将一个图片粘贴到另一个图片上，进行叠加，第一个参数表示要粘贴上来的图片，第二个参数是粘贴的边的位置，和原图片尺寸相同
    # image1 = Image.open('./black.jpg')
    # image1Crop = image1.crop(rect)
    # image1Crop.show()
    # image.paste(image1Crop, (200, 100, 600, 500))
    # image.show()

    # 翻转图片,旋转图片
    # image.rotate(90).show()
    # image.transpose(Image.FLIP_TOP_BOTTOM).show()
    # image.transpose(Image.FLIP_LEFT_RIGHT).show()

    # 操作像素
    for i in range(80, 210):
        for j in range(100, 400):
            image.putpixel((i, j), (255, 0, 0))
    image.show()

    # 滤镜处理,翻转像素
    image.filter(ImageFilter.CONTOUR).show()

if __name__ == '__main__':
    main()
