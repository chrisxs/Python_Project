import os
import sys

def execute_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Error executing command: {command}")
        sys.exit(1)

def wait_for_user():
    input("Press any key to continue...")

def join_network():
    network_id = input("Please enter the network ID: ")
    execute_command(f"zerotier-cli join {network_id}")

def list_networks():
    execute_command("zerotier-cli listnetworks")
    wait_for_user()

def orbit():
    moon_id = input("Please enter the moon ID: ")
    execute_command(f"zerotier-cli orbit {moon_id}")

def list_peers():
    execute_command("zerotier-cli peers")

def main():
    while True:
        print("Please choose an action:")
        print("1. Join a network")
        print("2. List networks")
        print("3. Orbit a moon")
        print("4. List peers")
        print("5. Exit")
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
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
