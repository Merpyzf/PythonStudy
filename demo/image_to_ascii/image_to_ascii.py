# coding:utf-8
from PIL import Image
import argparse

# 命令行输入参数处理

parser = argparse.ArgumentParser()
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=200)  # 输出字符的画宽
parser.add_argument('--height', type=int, default=200)  # 输出字符的画宽

# 获取参数

args = parser.parse_args()

img = args.file
img_width = args.width
img_height = args.height
img_output = args.output

# 获取运行时输入的参数
print img, img_width, img_height, img_output

# 灰度映射字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    # 计算灰度值
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(img)
    im = im.resize((img_width, img_height), Image.ANTIALIAS)
    txt = ""

    for i in range(img_height):
        for j in range(img_width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print txt

    if img_output:
        with open(img_output, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)

