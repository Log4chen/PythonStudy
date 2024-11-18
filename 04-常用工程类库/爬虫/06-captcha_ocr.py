from PIL import Image, ImageFilter
import pytesseract

'''
需要现在本机安装tesseract-ocr，并配置环境变量
'''
captcha = Image.open("captcha/captcha1.png")
result = pytesseract.image_to_string(captcha)
print(result)

# 灰度+二值化处理
def convert_img(img, threshold):
    img = img.convert("L")  # 处理灰度 L Luminance 亮度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

img = Image.open("captcha/captcha4.png")
result = pytesseract.image_to_string(img)
print(f'图片未经过处理的OCR结果：{result}')
# 灰度 + 二值化
# img = convert_img(img,150)
img = img.convert("L")  # 处理灰度 L Luminance 亮度
img.show()
# 二值化处理阈值
threshold = 150
# 遍历图像中的每个像素，如果像素值大于阈值，则将该像素设置为255（白色），否则设置为0（黑色）
img = img.point(lambda p: p > threshold and 255)
img.show()

# 去除噪点
img = img.filter(ImageFilter.MedianFilter(size=5))

img.show()
result = pytesseract.image_to_string(img)
print(f'图片经过处理的OCR结果：{result}')



