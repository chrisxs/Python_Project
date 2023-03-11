import platform
import psutil

# 检测操作系统和平台
if platform.system() == "Windows":
    import wmi
    c = wmi.WMI()
    system = c.Win32_OperatingSystem()[0]
    print("OS Name: ", system.Caption)
    print("Version: ", system.Version)
    print("Architecture: ", platform.machine())

elif platform.system() == "Linux":
    print("OS Name: ", platform.system())
    print("Version: ", platform.release())
    print("Architecture: ", platform.machine())

# 查询 CPU 信息
cpufreq = psutil.cpu_freq()
print(f"\n当前CPU最大频率：{cpufreq.max:.2f} MHz")
print(f"当前CPU最小频率：{cpufreq.min:.2f} MHz")
print(f"当前CPU使用频率：{cpufreq.current:.2f} MHz")

print("CPU核心数：", psutil.cpu_count(logical=True))

# 查询内存大小
svmem = psutil.virtual_memory()
print(f"\n总内存：{svmem.total / (1024**3):.3f} GB")
print(f"可用内存：{svmem.available / (1024**3):.3f} GB")

# 查询硬盘大小
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"\n分区名：{partition.device}")
    print(f"挂载点：{partition.mountpoint}")
    print(f"文件系统类型：{partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # 当前用户无权限访问
        continue
    print(f"总大小：{partition_usage.total / (1024**3):.3f} GB")
    print(f"已用大小：{partition_usage.used / (1024**3):.3f} GB")
    print(f"可用大小：{partition_usage.free / (1024**3):.3f} GB")

# 查询网络适配器信息
net_io_counters = psutil.net_io_counters()
#print(f"总接收数据包数：{net_io_counters.packets_recv}")
#print(f"总发送数据包数：{net_io_counters.packets_sent}")
print("\n网络适配器信息：")
net_if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in net_if_addrs.items():
    for address in interface_addresses:
        print(f"适配器名称：{interface_name}")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"IP地址：{address.address}")
            print(f"子网掩码：{address.netmask}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
           if str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"MAC地址：{address.address}")
            print(f"地址族：{address.family}")
            
input("\n按任意键退出")
