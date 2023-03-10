import sys

def calculate_storage():
    # 输出选择项
    print("请选择计算条件：")
    print("1. 分辨率")
    print("2. 码率")
    # 读取用户输入
    while True:
        try:
            option = int(input())
            if option == 1:
                print("请选择编码类型：")
                print("1. H.264")
                print("2. H.265")
                encoding = int(input())
                if encoding not in [1, 2]:
                    raise ValueError("输入的编码类型不正确，请重新输入")
                print("请选择分辨率：")
                print("1. 720p")
                print("2. 1080p")
                resolution = int(input())
                if resolution not in [1, 2]:
                    raise ValueError("输入的分辨率不正确，请重新输入")
                print("请输入摄像头数量：")
                camera_num = int(input())
                print("请输入计划录像天数：")
                days = int(input())
                if days <= 0:
                    raise ValueError("计划录像天数必须大于0，请重新输入")
                if encoding == 1 and resolution == 1:
                    reference = 23.20
                elif encoding == 2 and resolution == 1:
                    reference = 11.6
                elif encoding == 1 and resolution == 2:
                    reference = 46.41
                elif encoding == 2 and resolution == 2:
                    reference = 23.20
                storage = round(camera_num * reference * days, 2)
                unit = "GB"
                if storage > 1024:
                    storage /= 1024
                    unit = "TB"
                print(f"需要的硬盘容量为：{storage:.2f}{unit}")
                break
            elif option == 2:
                print("请输入摄像头数量：")
                camera_num = int(input())
                print("请输入计划录像天数：")
                days = int(input())
                if days <= 0:
                    raise ValueError("计划录像天数必须大于0，请重新输入")
                print("请输入每个摄像头的码率（Mbps）：")
                bitrate = float(input())
                reference = 11.6
                storage = round(camera_num * bitrate * reference * days, 2)
                unit = "GB"
                if storage > 1024:
                    storage /= 1024
                    unit = "TB"
                print(f"需要的硬盘容量为：{storage:.2f}{unit}")
                break
            else:
                raise ValueError("输入的选项不正确，请重新输入")
        except ValueError as e:
            print("输入的内容不正确，请重新输入")
            print(str(e))
            continue

if __name__ == "__main__":
    while True:
        calculate_storage()
        choice = input("是否重新运行程序？(Y/N)").strip().lower()
        if choice != 'y':
            break
    sys.exit(0)
