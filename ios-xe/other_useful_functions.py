# Import Netmiko's ConnectHandler
from netmiko import ConnectHandler


def main():
    # Create a device dictionary
    ios_xe = {
        "device_type": "cisco_xe",
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22
    }

    # Establish SSH connect, passing in the device dictionary
    net_connect = ConnectHandler(**ios_xe)

    prompt = net_connect.find_prompt()
    print(prompt)

    # Disconnect from SSH Session
    net_connect.disconnect()


if __name__ == "__main__":
    main()
