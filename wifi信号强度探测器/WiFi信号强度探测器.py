import time
from tkinter import *
import csv
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#subprocess.call('chcp 65001', shell=True)
#subprocess.call('netsh wlan show interface', shell=True)
#time.sleep(1)

def get_wireless_interfaces():
    # 获取可用的无线网卡列表
    cmd = 'netsh wlan show interface'
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate()
    interfaces = []
    for line in output.split('\n'):
        line = line.strip()
        if line.startswith('名称'):
            interface = line.split(':')[-1].strip()
            interfaces.append(interface)
    return interfaces


def scan(interface):
    # 扫描指定无线网卡可探测到的 Wi-Fi SSID
    cmd = f'netsh wlan show networks interface="{interface}" mode=Bssid'
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate()
    ssid_rssi_list = []
    ssid, rssi = '', ''
    for line in output.split('\n'):
        line = line.strip()
        if line.startswith('SSID'):
            ssid = line.split(':')[1].strip()
        elif line.startswith('信号'):
            rssi = int(line.split(':')[1].strip().replace('%', ''))
        elif line.startswith('BSSID'):
            ssid_rssi_list.append((ssid, rssi))
    return ssid_rssi_list


if __name__ == '__main__':
    interfaces = get_wireless_interfaces()
    if not interfaces:
        print('未发现无线网卡')
    else:
        print('可用的无线网卡：')
        for i, interface in enumerate(interfaces):
            print(f'{i + 1}. {interface}')

        # 选择无线网卡
        interface_idx = int(input(f'请选择无线网卡（输入编号，范围：1~{len(interfaces)}）：'))
        interface = interfaces[interface_idx - 1]

        # 扫描 Wi-Fi SSID
        ssid_rssi_list = scan(interface)
        if not ssid_rssi_list:
            print(f'未探测到任何 Wi-Fi SSID')
        else:
            # 打印扫描结果
            print(f'{interface} 可探测到的 Wi-Fi SSID 及其信号强度：')
            for ssid, rssi in ssid_rssi_list:
                print(f'{ssid}：{rssi}%')

            # 将结果保存到 CSV 文件
            df = pd.DataFrame(ssid_rssi_list, columns=['SSID', 'RSSI'])
            # 转换 RSSI 列为数字类型
            df['RSSI'] = pd.to_numeric(
                df['RSSI'], errors='coerce').fillna(0).astype(int)
            filename = f'{interface}_scan_results.csv'
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            print(f'扫描结果已保存到 {filename}')

            # 绘制柱状图
            df.plot.bar(x='SSID', y='RSSI', rot=0)
            plt.title(f'{interface} Wi-Fi RSSI Scan Results')
            plt.xlabel('SSID')
            plt.ylabel('RSSI (%)')
            plt.tight_layout()
            plt.show()