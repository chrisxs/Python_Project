import os
import sys
import subprocess


print("zerotier傻瓜化脚本：请在管理员身份下运行来源：chrisxs.com")
print("来源：chrisxs.com")
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True)
        if result.returncode != 0:
            print(f"Command failed with return code {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"错误信息: {e}")

def wait_for_user():
    input("请按任意键继续...")

def join_network():
    network_id = input("请输入网络 ID: ")
    execute_command(f"zerotier-cli join {network_id}")

def list_networks():
    execute_command("zerotier-cli listnetworks")
#    wait_for_user()

def orbit():
    moon_id = input("请输入moon ID: ")
    execute_command(f"zerotier-cli orbit {moon_id}")

def list_peers():
    execute_command("zerotier-cli peers")

def main():
    execute_command(f"chcp 65001")
    while True:
        print("请选择操作:")
        print("1. 加入网络")
        print("2. 查看已加入网络信息")
        print("3. 加入moon")
        print("4. 查看详情")
        print("5. 退出程序")
        choice = input()

        if choice == "1":
            join_network()
        elif choice == "2":
            list_networks()
        elif choice == "3":
            orbit()
        elif choice == "4":
            list_peers()
        elif choice == "5":
            break
        else:
            print("选择无效，请重新选择.")

if __name__ == "__main__":
    main()
