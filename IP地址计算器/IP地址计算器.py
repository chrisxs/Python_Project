import ipaddress
import csv

def get_subnet_info(ip_address, subnet_mask):
    # 计算CIDR
    net = ipaddress.ip_network(ip_address + '/' + subnet_mask, strict=False)
    cidr = net.prefixlen

    # 计算主机总数
    num_hosts = net.num_addresses - 2

    # 计算网络地址、最大地址、最小地址和广播地址
    net_address = str(net.network_address)
    max_address = str(net.broadcast_address - 1)
    min_address = str(net.network_address + 1)
    broadcast_address = str(net.broadcast_address)

    return [ip_address, subnet_mask, cidr, net_address, num_hosts, max_address, min_address, broadcast_address]

def main():
    # 获取用户输入
    ip_address = input("请输入IP地址：")
    subnet_mask = input("请输入子网掩码：")

    try:
        # 计算子网信息
        subnet_info = get_subnet_info(ip_address, subnet_mask)

        # 输出结果
        print(f"CIDR: {subnet_info[2]}")
        print(f"网络地址: {subnet_info[3]}")
        print(f"主机总数: {subnet_info[4]}")
        print(f"最大地址: {subnet_info[5]}")
        print(f"最小地址: {subnet_info[6]}")
        print(f"广播地址: {subnet_info[7]}")

        # 导出到CSV文件
        filename = "subnet_info.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['属性', '值'])
            writer.writerow(['IP地址', subnet_info[0]])
            writer.writerow(['子网掩码', subnet_info[1]])
            writer.writerow(['CIDR', subnet_info[2]])
            writer.writerow(['网络地址', subnet_info[3]])
            writer.writerow(['主机总数', subnet_info[4]])
            writer.writerow(['最大地址', subnet_info[5]])
            writer.writerow(['最小地址', subnet_info[6]])
            writer.writerow(['广播地址', subnet_info[7]])
        print(f"子网信息已导出到文件: {filename}")

        # 询问用户是否继续
        while True:
            choice = input("是否重新启动程序? (Y/N): ").upper()
            if choice == 'Y':
                main()
                break
            elif choice == 'N':
                break
            else:
                print("请输入Y或N。")

    except ValueError as e:
        print("错误: ", e)
        main()

if __name__ == '__main__':
    main()
