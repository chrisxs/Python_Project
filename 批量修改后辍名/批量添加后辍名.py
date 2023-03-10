import os

# 指定需要修改后缀名的目录路径
path = "D:/Seafile/3-常用软件/9-python自动化办公/批量修改后辍名/新建文件夹"

# 获取指定目录下所有文件的列表
files = os.listdir(path)

# 循环遍历所有文件
for file in files:
    # 如果文件名中包含"."，说明是文件而不是文件夹
    if "." in file:
        # 将文件名和后缀名分开
        filename, ext = os.path.splitext(file)
        # 如果后缀名不是.gif，则修改后缀名
        if ext != ".gif":
            new_file = os.path.join(path, filename + ".gif")
            os.rename(os.path.join(path, file), new_file)
            print(f"将文件 {file} 的后缀名修改为 .gif")
    else:
        # 如果文件名中不包含"."，则添加后缀名为.gif
        new_file = os.path.join(path, file + ".gif")
        os.rename(os.path.join(path, file), new_file)
        print(f"将文件 {file} 添加后缀名 .gif")

