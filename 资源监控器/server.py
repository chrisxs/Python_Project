import socket
import json
import tkinter as tk
from tkinter import ttk
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# 设置监听端口
host = "192.168.31.242"  # 本地IP地址，与被监控主机通信时的监听地址
port = 9999              # 本地监听端口
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

# GUI设置
root = tk.Tk()
root.title("System Monitoring")
root.geometry("1000x400")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# 创建Treeview表格
treeview = ttk.Treeview(frame, columns=(
    "Source IP", "CPU Usage (%)", "CPU Temp (°C)", "Memory Usage (%)",
    "GPU Usage (%)", "GPU Temp (°C)", "Disk IO Read (MB/s)", "Disk IO Write (MB/s)"
), show="headings")

# 配置列标题
treeview.heading("Source IP", text="Source IP")
treeview.heading("CPU Usage (%)", text="CPU Usage (%)")
treeview.heading("CPU Temp (°C)", text="CPU Temp (°C)")
treeview.heading("Memory Usage (%)", text="Memory Usage (%)")
treeview.heading("GPU Usage (%)", text="GPU Usage (%)")
treeview.heading("GPU Temp (°C)", text="GPU Temp (°C)")
treeview.heading("Disk IO Read (MB/s)", text="Disk IO Read (MB/s)")
treeview.heading("Disk IO Write (MB/s)", text="Disk IO Write (MB/s)")

# 配置列宽
treeview.column("Source IP", width=120)
treeview.column("CPU Usage (%)", width=100)
treeview.column("CPU Temp (°C)", width=100)
treeview.column("Memory Usage (%)", width=120)
treeview.column("GPU Usage (%)", width=120)
treeview.column("GPU Temp (°C)", width=120)
treeview.column("Disk IO Read (MB/s)", width=120)
treeview.column("Disk IO Write (MB/s)", width=120)

treeview.pack(fill=tk.BOTH, expand=True)

# 用于并发接收数据的线程池
executor = ThreadPoolExecutor(max_workers=10)

# 用于存储被监控端的数据
system_data = {}

def fetch_data():
    """接收并处理数据"""
    while True:
        data, addr = sock.recvfrom(1024)  # 接收数据
        source_ip = addr[0]
        try:
            system_info = json.loads(data.decode('utf-8'))  # 解码JSON数据
        except json.JSONDecodeError:
            print(f"Malformed data from {source_ip}: {data.decode('utf-8')}")
            continue
        
        # 更新系统数据字典
        system_data[source_ip] = system_info
        
        # 更新GUI
        update_table()

def update_table():
    """更新GUI上的表格数据"""
    # 清空现有数据，避免重复显示
    for row in treeview.get_children():
        treeview.delete(row)
    
    # 插入每个被监控端的数据
    for source_ip, system_info in system_data.items():
        # 获取硬盘读写速度
        disk_io_speed = system_info.get('disk_io_speed', {})
        disk_io_read = sum(disk['read_speed'] for disk in disk_io_speed.values())
        disk_io_write = sum(disk['write_speed'] for disk in disk_io_speed.values())

        treeview.insert("", "end", values=(
            source_ip,
            f"{system_info.get('cpu_usage', 'N/A'):.2f}",
            system_info.get('cpu_temp', 'N/A') if system_info.get('cpu_temp') is not None else "N/A",
            f"{system_info.get('memory_usage', 'N/A'):.2f}",
            f"{system_info.get('gpu_usage', 'N/A'):.2f}" if system_info.get('gpu_usage') is not None else "N/A",
            system_info.get('gpu_temp', 'N/A') if system_info.get('gpu_temp') is not None else "N/A",
            f"{disk_io_read:.2f}" if disk_io_read else "N/A",
            f"{disk_io_write:.2f}" if disk_io_write else "N/A"
        ))

# 启动接收数据的线程
executor.submit(fetch_data)

# 启动GUI事件循环
root.mainloop()