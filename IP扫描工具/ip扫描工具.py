import os
import socket
import threading
from ipaddress import IPv4Network
from tqdm import tqdm

def scan_ip(ip):
    response = os.system("ping -c 1 -w 1 " + str(ip))
    if response == 0:
        return False
    else:
        return True

def scan_network(network, event):
    used_ips = []
    free_ips = []
    for ip in network:
        if scan_ip(str(ip)):
            used_ips.append(str(ip))
        else:
            free_ips.append(str(ip))
    print("Used IPs:", used_ips)
    print("Free IPs:", free_ips)
    event.set()

def main():
    while True:
        subnet = input("请输入网络段(例如，192.168.1.0/24):")
        try:
            network = IPv4Network(subnet, strict=False)
        except ValueError:
            print("无效的IP地址格式，请重试。")
            continue
        event = threading.Event()
        scan_thread = threading.Thread(target=lambda: scan_network(network, event))
        scan_thread.start()
        event.wait()
        scan_thread.join()  # 等待子线程完成
        choice = input("是否要再次运行程序？(y/n):")
        if choice.lower() != "y":
            break

if __name__ == "__main__":
    main()
