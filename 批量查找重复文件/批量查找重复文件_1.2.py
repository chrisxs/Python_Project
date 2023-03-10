import os
import hashlib
import shutil

# 计算文件的MD5值
def md5(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        md5_value = hashlib.md5(data).hexdigest()
        return md5_value

# 搜索指定路径下的所有文件
def search_files(path):
    files_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            md5_value = md5(file_path)
            if md5_value in files_dict:
                files_dict[md5_value].append(file_path)
            else:
                files_dict[md5_value] = [file_path]
    return files_dict

# 移动重复的文件到指定目录，并保留文件名最短的文件
def move_duplicates(duplicates, move_path):
    for md5_value, file_list in duplicates.items():
        if len(file_list) > 1:
            shortest_file = min(file_list, key=len)
            for file_path in file_list:
                if file_path != shortest_file:
                    try:
                        shutil.move(file_path, os.path.join(move_path, os.path.basename(file_path)))
                    except:
                        print(f"Error moving file: {file_path}")

# 恢复文件
def restore_files(duplicates):
    for md5_value, file_list in duplicates.items():
        if len(file_list) > 1:
            shortest_file = min(file_list, key=len)
            for file_path in file_list:
                if file_path != shortest_file:
                    try:
                        shutil.move(os.path.join("重复文件", os.path.basename(file_path)), file_path)
                    except:
                        print(f"Error restoring file: {file_path}")

# 主程序
if __name__ == '__main__':
    path = input("请输入要搜索的文件夹路径：")
    if not path:
        path = "."

    files_dict = search_files(path)

    # 打印出所有重复的文件
    duplicates = {k:v for k,v in files_dict.items() if len(v)>1}
    if len(duplicates) > 0:
        print("以下文件是重复的：")
        for md5_value, file_list in duplicates.items():
            print(f"MD5值为 {md5_value} 的文件有以下重复：")
            for file_path in file_list:
                print(file_path)
    else:
        print("没有重复的文件！")
        exit()

    # 询问用户是否要继续
    choice = input("是否要移动这些文件到重复文件夹？（是/否）：")
    if choice.lower() == '是':
        if not os.path.exists("重复文件"):
            try:
                os.mkdir("重复文件")
            except:
                print("创建目录失败！")
                exit()

        move_duplicates(duplicates, "重复文件")
        print("文件已经移动到重复文件夹！")

        # 询问用户是否已经正确处理
        choice = input("文件是否已经正确处理？（是/否）：")
        if choice.lower() == '否':
            restore_files(duplicates)
            print("文件已经恢复！")
    else:
        print("文件没有移动！")

    input("按任意键退出！")
