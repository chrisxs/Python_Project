import pandas as pd
import os
import time

# 获取程序所在目录的路径
program_dir = os.path.dirname(os.path.abspath(__file__))

# 让用户输入要读取的Excel文件的名称
while True:
    try:
        filename = input("请输入要读取的Excel文件的名称：")
        # 检查文件是否存在
        if not os.path.exists(os.path.join(program_dir, filename)):
            raise FileNotFoundError
        break
    except FileNotFoundError:
        print("文件不存在，请重新输入。")
    except Exception as e:
        print("发生错误：", e)

# 让用户输入要添加的字符串
add_str = input("请输入要添加的字符串：")

# 读取Excel文件
df = pd.read_excel(os.path.join(program_dir, filename))

# 在每个单元格中添加字符串
for i in range(len(df)):
    for j in range(len(df.columns)):
         df.iloc[i, j] = str(df.iloc[i, j]) + " " + add_str

# 保存修改后的Excel文件
now = time.strftime("%Y%m%d%H%M%S", time.localtime())
new_filename = filename.split(".")[0] + "_" + now + ".xlsx"
new_file_path = os.path.join(program_dir, new_filename)
df.to_excel(new_file_path, index=False)

print("文件已保存在：", new_file_path)
