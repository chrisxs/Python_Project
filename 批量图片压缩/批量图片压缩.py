import os
from PIL import Image

# 获取当前工作目录
cwd = os.getcwd()

# 获取当前目录下的所有图片文件
image_files = [f for f in os.listdir(cwd) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

if not image_files:
    print("没有找到图片文件。")
else:
    # 获取压缩百分比
    percent = None
    while percent is None:
        try:
            percent = int(input("请输入要压缩的百分比（例如 50 表示压缩到原来的 50%）："))
            if percent <= 0 or percent > 100:
                print("压缩百分比必须在 1 到 100 之间，请重新输入。")
                percent = None
        except ValueError:
            print("输入的值不合法，请输入一个整数。")
    
    # 遍历所有图片文件并进行压缩
    for file in image_files:
        image_path = os.path.join(cwd, file)
        with Image.open(image_path) as img:
            # 获取压缩后的尺寸
            width, height = img.size
            width = int(width * percent / 100)
            height = int(height * percent / 100)
            # 进行压缩
            img = img.resize((width, height), resample=Image.LANCZOS)
            # 保存压缩后的文件
            compressed_file = os.path.splitext(file)[0] + '_compressed.jpg'
            img.save(compressed_file)
            print(f'{file} 压缩完成，已保存为 {compressed_file}。')

