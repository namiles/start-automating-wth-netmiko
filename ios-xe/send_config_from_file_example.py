# Import Netmiko's ConnectHandler
from netmiko import ConnectHandler


def main():
    # Create a device dictionary
    ios_xe = {
        "device_type": "cisco_xe",
        "host": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 22,
        "session_log": "iosxe_config_file_log.log",
    }

    # Establish SSH connect, passing in the device dictionary
    net_connect = ConnectHandler(**ios_xe)

    # Run config commands from file
    print("Creating loopback511")
    net_connect.send_config_from_file("commands.txt")

    # Run "show ip int brief" to verify
    output = net_connect.send_command("show ip int brief")
    print(output)

    # Always clean up your config!
    print("\nRemoving loopback511")
    cleanup_commands = ["no int loopback511"]
    net_connect.send_config_set(cleanup_commands)

    # Run "show ip int brief" to verify config is removed
    output = net_connect.send_command("show ip int brief")
    print(output)

    # Disconnect from SSH Session
    net_connect.disconnect()


if __name__ == "__main__":
    main()
