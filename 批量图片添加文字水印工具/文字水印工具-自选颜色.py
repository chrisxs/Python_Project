from os import listdir
from os.path import isfile, join
from PIL import Image, ImageDraw, ImageFont
import warnings

print("批量图片水印添加工具，来源：chrisxs.com \n")
try:
    # 获取用户输入的水印文字、水印文字间隔、水印文字角度和水印文字透明度
    watermark_text = input("请输入水印文字：")
    watermark_spacing = int(input("请输入水印文字间隔（默认为0）：") or "0")
    watermark_angle = int(input("请输入水印文字角度（默认为0）：") or "0")
    watermark_opacity = int(input("请输入水印文字透明度（0-255，默认为128）：") or "128")
    watermark_color_choice = input("请选择水印文字颜色（1-红色，2-灰色，3-白色，默认为2）：") or "2"

    # 根据用户选择的颜色设置水印文字的颜色
    if watermark_color_choice == "1":
        watermark_color = (255, 0, 0, watermark_opacity)
    elif watermark_color_choice == "3":
        watermark_color = (255, 255, 255, watermark_opacity)
    else:
        watermark_color = (128, 128, 128, watermark_opacity)

    # 获取当前目录下的所有图片文件
    files = [f for f in listdir(".") if isfile(join(".", f)) and f.endswith((".jpg", ".jpeg", ".png"))]

    # 遍历每个图片文件，添加文字水印并保存
    for file in files:
        # 打开图片文件
        with Image.open(file) as img:
            # 获取图片宽度和高度
            width, height = img.size

            # 创建一个与图片相同大小的画布
            canvas = ImageDraw.Draw(img)

            # 设置水印文字的字体和大小
            font = ImageFont.truetype("arial.ttf", int(min(width, height) * 0.05))

            # 计算水印文字的宽度和高度
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                text_width, text_height = canvas.textsize(watermark_text, font)

            # 计算水印文字的倾斜角度
            angle = watermark_angle % 360

            # 计算水印文字的透明度
            opacity = int(watermark_opacity)
            # 在图片上平铺添加水印文字
            for x in range(0, width, text_width + watermark_spacing):
                for y in range(0, height, text_height + watermark_spacing):
                    # 旋转水印文字
                    rotated_text = Image.new("RGBA", (text_width, text_height), (255, 255, 255, 0))
                    rotated_text_draw = ImageDraw.Draw(rotated_text)
                    rotated_text_draw.text((0, 0), watermark_text, fill=watermark_color, font=font)
                    rotated_text = rotated_text.rotate(angle, expand=True)

                    # 计算水印文字的位置和透明度
                    pos = (x, y)
                    alpha = rotated_text.convert("RGBA").getchannel
                    # 计算水印文字的位置和透明度
                    pos = (x, y)
                    alpha = rotated_text.convert("RGBA").getchannel(3)
                    alpha = alpha.point(lambda i: i * opacity / 255)
                    rotated_text.putalpha(alpha)

                    # 将水印文字添加到图片上
                    img.paste(rotated_text, pos, rotated_text)

            # 保存添加水印后的图片
            img.save(f"watermarked_{file}")
    print("水印添加完成！")
except Exception as e:
    print("程序出现错误：", e)
    
input("按任意键退出程序")
