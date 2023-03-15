import os
import fitz

def add_watermark_to_pdf(pdf_path, watermark_text, rotation_angle, opacity, color):
    # 打开PDF文件
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            # 创建文本框
            textbox = fitz.Rect(0, 0, 300, 50)
            # 设置文本样式
            text_style = fitz.TextStyle()
            text_style.fontname = "Arial"
            text_style.fontsize = 50
            if color == 1:
                text_style.fill = (1, 0, 0)  # 红色
            elif color == 2:
                text_style.fill = (0.5, 0.5, 0.5)  # 灰色
            else:
                text_style.fill = (1, 1, 1)  # 白色
            # 旋转文本框
            textbox.transform(fitz.Matrix(1, 0, 0, 1, 0, 0).preRotate(rotation_angle))
            # 插入文本
            page.insertTextbox(textbox, watermark_text, fontsize=text_style.fontsize, fontname=text_style.fontname, color=text_style.fill)
            # 调整文本透明度
            watermark_obj = page.get_textbox_page_number(textbox)
            watermark_obj.update(overlay=True, opacity=opacity)

        # 保存修改后的PDF文件
        pdf.save(pdf_path[:-4] + '_watermark.pdf')
    print(f"已将水印添加到PDF文件 {pdf_path} 中。")

if __name__ == '__main__':
    # 获取用户输入
    watermark_text = input("请输入水印文字：")
    rotation_angle = int(input("请输入旋转角度（0-360）："))
    opacity = int(input("请输入透明度（0-255）："))
    color = int(input("请选择水印颜色（1.红色 2.灰色 3.白色）："))

    # 遍历当前目录下所有PDF文件，为每个文件添加水印
    for filename in os.listdir():
        if filename.endswith(".pdf"):
            add_watermark_to_pdf(filename, watermark_text, rotation_angle, opacity, color)

    input("水印添加完成，按任意键退出。")
