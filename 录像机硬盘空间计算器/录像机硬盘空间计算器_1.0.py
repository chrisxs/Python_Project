def resolution_to_factor(resolution):
    if resolution == 1:
        return 1.0
    elif resolution == 2:
        return 1.5
    elif resolution == 3:
        return 2.0
    elif resolution == 4:
        return 2.5
    elif resolution == 5:
        return 4.0
    elif resolution == 6:
        return 5.0
    else:
        return 0.0


def main():
    num_channels = int(input("请输入通道数量: "))
    num_days = int(input("请输入计划录制天数: "))
    bitrate = float(input("请输入摄像机码率(Mbps): "))
    print("请选择分辨率和压缩类型:")
    print("1: 1280x720 H.264")
    print("2: 1280x720 H.265")
    print("3: 1920x1080 H.264")
    print("4: 1920x1080 H.265")
    print("5: 3840x2160 H.264")
    print("6: 3840x2160 H.265")
    resolution = int(input("请选择序号: "))
    factor = resolution_to_factor(resolution)
    hourly_size = bitrate * 60 * 60 * num_channels * factor / 8 / 1024
    daily_size = hourly_size * 24
    total_size = daily_size * num_days / 1024
    print("每小时所需硬盘空间: %.2f GB" % hourly_size)
    print("每天所需硬盘空间: %.2f GB" % daily_size)
    print("需要的总硬盘空间: %.2f TB" % total_size)


if __name__ == '__main__':
    main()
