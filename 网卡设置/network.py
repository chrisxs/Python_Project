import subprocess
import re

# 获取所有网络适配器名称和索引
ipconfig_output = subprocess.check_output('ipconfig /all', shell=True)
adapter_names = re.findall('适配器 (.*):', ipconfig_output.decode('gb2312'))

# 用户选择要更改的适配器
print('请选择要更改的网络适配器：')
for i, adapter_name in enumerate(adapter_names):
    print(f'{i+1}. {adapter_name}')
selection = int(input()) - 1
adapter_name = adapter_names[selection]

# 用户输入新的IP地址、子网掩码、网关和DNS
ip_address = input('请输入新的IP地址（留空使用 DHCP 获取）：').strip()
subnet_mask = input('请输入新的子网掩码（留空使用 DHCP 获取）：').strip()
gateway = input('请输入新的网关（留空使用 DHCP 获取）：').strip()
dns = input('请输入新的 DNS（留空使用 DHCP 获取）：').strip()

# 检查是否使用 DHCP 获取网络设置
use_dhcp = not any([ip_address, subnet_mask, gateway, dns])

# 使用Windows命令行命令更改网络适配器设置
if use_dhcp:
    subprocess.run(
        f'netsh interface ipv4 set address "{adapter_name}" dhcp', shell=True)
    subprocess.run(
        f'netsh interface ipv4 set dns "{adapter_name}" dhcp', shell=True)
    print(f'{adapter_name}的IP地址和DNS已更改为 DHCP 获取。')
else:
    subprocess.run(
        f'netsh interface ipv4 set address "{adapter_name}" static {ip_address} {subnet_mask} {gateway} 1', shell=True)
    subprocess.run(
        f'netsh interface ipv4 set dns "{adapter_name}" static {dns} primary', shell=True)
    print(f'{adapter_name}的IP地址已更改为{ip_address}，子网掩码为{subnet_mask}，网关为{gateway}，DNS为{dns}。')