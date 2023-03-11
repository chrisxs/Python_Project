import ipaddress
import random
import csv

def calculate_subnet_mask(num_hosts):
    """
    根据主机数量计算适用的子网掩码
    """
    for i in range(32, 0, -1):
        if (2 ** i - 2) >= num_hosts:
            return str(ipaddress.IPv4Network(f"0.0.0.0/{i}").netmask)

def generate_ip_address():
    """
    随机生成IP地址
    """
    ip = ipaddress.IPv4Address(random.randint(0, 2**32-1))
    return str(ip)

def generate_network(ip_address, subnet_mask):
    """
    根据IP地址和子网掩码生成网络
    """
    return str(ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}"))

def calculate_max_address(network):
    """
    根据网络地址计算最大地址
    """
    return str(ipaddress.IPv4Address(int(network.network_address) + network.num_addresses - 2))

def calculate_min_address(network):
    """
    根据网络地址计算最小地址
    """
    return str(ipaddress.IPv4Address(int(network.network_address) + 1))

def calculate_broadcast_address(network):
    """
    根据网络地址计算广播地址
    """
    return str(network.broadcast_address)

def main():
    try:
        num_hosts = int(input("请输入主机数量: "))
        subnet_mask = calculate_subnet_mask(num_hosts)
        ip_address = generate_ip_address()
        network = generate_network(ip_address, subnet_mask)
        max_address = calculate_max_address(network)
        min_address = calculate_min_address(network)
        broadcast_address = calculate_broadcast_address(network)
        total_hosts = network.num_addresses - 2

        print(f"IP地址: {ip_address}")
        print(f"子网掩码CIDR: /{subnet_mask.count('1')}")
        print(f"网络: {network}")
        print(f"主机总数: {total_hosts}")
        print(f"最大地址: {max_address}")
        print(f"最小地址: {min_address}")
        print(f"广播地址: {broadcast_address}")

        # 导出结果到CSV文件
        with open("result.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["IP地址", "子网掩码CIDR", "网络", "主机总数", "最大地址", "最小地址", "广播地址"])
            writer.writerow([ip_address, f"/{subnet_mask.count('1')}", network, total_hosts, max_address, min_address, broadcast_address])
        
        restart = input("计算完成，是否重新启动程序？(Y/N): ").strip().lower() == "y"
        if restart:
            main()
    except ValueError:
        print("请输入一个整数作为主机数量")
        main()

if __name__ == "__main__":
    main()
