import os
import hashlib
import shutil
import sys

print('      批量查找重复文件工具')
print('*****请在操作前备份你的数据！*****')
print('       来源：chrisxs.com')
# 计算文件的MD5值


def md5(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        md5_value = hashlib.md5(data).hexdigest()
        return md5_value
# 搜索指定路径下的所有文件


def search_files(path):
    files_dict = {}
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            md5_value = md5(file_path)
            if md5_value in files_dict:
                files_dict[md5_value].append(file_path)
            else:
                files_dict[md5_value] = [file_path]
            count += 1
            # 显示搜索进度
            sys.stdout.write(f"\r正在搜索文件，已搜索 {count} 个文件...")
            sys.stdout.flush()
    sys.stdout.write("\n")
    return files_dict

# 移动重复的文件到指定目录，并保留文件名最短的文件


def move_duplicates(duplicates, move_path):
    count = 0
    for md5_value, file_list in duplicates.items():
        if len(file_list) > 1:
            shortest_file = min(file_list, key=len)
            for file_path in file_list:
                if file_path != shortest_file:
                    try:
                        shutil.move(file_path, os.path.join(
                            move_path, os.path.basename(file_path)))
                        count += 1
                        # 显示移动进度
                        sys.stdout.write(f"\r正在移动文件，已移动 {count} 个文件...")
                        sys.stdout.flush()
                    except:
                        print(f"Error moving file: {file_path}")
    sys.stdout.write("\n")

# 恢复文件


def restore_files(duplicates):
    count = 0
    for md5_value, file_list in duplicates.items():
        if len(file_list) > 1:
            shortest_file = min(file_list, key=len)
            for file_path in file_list:
                if file_path != shortest_file:
                    try:
                        shutil.move(os.path.join(
                            "重复文件", os.path.basename(file_path)), file_path)
                        count += 1
                        # 显示恢复进度
                        sys.stdout.write(f"\r\n正在恢复文件，已恢复 {count} 个文件...")
                        sys.stdout.flush()
                    except:
                        print(f"Error restoring file: {file_path}")
    sys.stdout.write("\n")


# 主程序
if __name__ == '__main__':
    path = input("\n请输入要搜索的文件夹路径（留空则直接按下“enter”键）：")
    if not path:
        path = "."

    files_dict = search_files(path)

    # 打印出所有重复的文件
    duplicates = {k: v for k, v in files_dict.items() if len(v) > 1}
    if len(duplicates) > 0:
        print("\n以下文件是重复的：")
        for md5_value, file_list in duplicates.items():
            print(f"\nMD5值为 {md5_value} 的文件有以下重复：")
            for file_path in file_list:
                print(file_path)
    else:
        print("\n没有重复的文件！")
        input("\n按任意键退出！")
        exit()

    # 询问用户是否要继续
    choice = input("\n是否要移动这些文件到“重复文件夹”\n(如果不存在该目录在本目录下新建)？\n是：输入y，否：输入n（y/n）：")
    if choice.lower() == 'y':
        if not os.path.exists("重复文件"):
            try:
                os.mkdir("重复文件")
            except:
                print("创建目录失败！")
                exit()

        move_duplicates(duplicates, "重复文件")
        print("\n文件已经移动到重复文件夹！")

        # 询问用户是否已经正确处理
        choice = input("\n文件是否已经正确处理？是：输入y，否：输入n（y/n）：")
        if choice.lower() == 'n':
            restore_files(duplicates)
            print("\n文件已经恢复原来位置！")
    else:
        print("\n文件没有移动！")

    input("\n按任意键退出！")
