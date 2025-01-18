import psutil
import socket
import time
import json
import GPUtil

def get_disk_io_speed():
    """获取硬盘各分区的读写速度 (MB/s)"""
    disk_io = psutil.disk_io_counters(perdisk=True)
    disk_io_speed = {}
    # 保存上次的读写字节数
    prev_io = {disk: io for disk, io in disk_io.items()}
    
    time.sleep(1)  # 暂停1秒以便计算增量

    # 获取当前的读写字节数
    current_io = psutil.disk_io_counters(perdisk=True)

    for disk, prev in prev_io.items():
        current = current_io.get(disk, None)
        if current:
            # 计算增量，单位字节
            read_speed = (current.read_bytes - prev.read_bytes) / (1024 * 1024)  # 转换为MB
            write_speed = (current.write_bytes - prev.write_bytes) / (1024 * 1024)  # 转换为MB
            disk_io_speed[disk] = {
                'read_speed': read_speed,
                'write_speed': write_speed
            }
    
    return disk_io_speed

def get_system_info():
    """获取系统信息"""
    # 获取 CPU 使用率
    cpu_usage = psutil.cpu_percent(interval=1)

    # 获取 CPU 温度
    try:
        cpu_temp = psutil.sensors_temperatures().get('coretemp', [{}])[0].get('current', None)
    except Exception:
        cpu_temp = None

    # 获取内存使用率
    memory_usage = psutil.virtual_memory().percent

    # 获取 GPU 信息
    gpu_info = GPUtil.getGPUs()
    gpu_usage = gpu_info[0].load * 100 if gpu_info else None
    gpu_temp = gpu_info[0].temperature if gpu_info else None

    # 获取硬盘读写速度
    disk_io_speed = get_disk_io_speed()

    # 获取计算机名
    hostname = socket.gethostname()  # 获取计算机名

    return {
        "cpu_usage": cpu_usage,
        "cpu_temp": cpu_temp,
        "memory_usage": memory_usage,
        "gpu_usage": gpu_usage,
        "gpu_temp": gpu_temp,
        "disk_io_speed": disk_io_speed,
        "hostname": hostname  # 添加计算机名
    }

def main():
    host = "192.168.31.242"  # 监控主机的IP地址
    port = 9999              # 监控主机的端口
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        data = get_system_info()
        try:
            sock.sendto(json.dumps(data).encode('utf-8'), (host, port))
            time.sleep(5)  # 每5秒发送一次
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
