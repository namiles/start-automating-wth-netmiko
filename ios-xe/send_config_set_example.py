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
        "session_log": "iosxe_config_set_log.log",
    }

    # Establish SSH connect, passing in the device dictionary
    net_connect = ConnectHandler(**ios_xe)

    # Create list of commands
    config_commands = ["int loopback510", "ip address 5.10.10.10 255.255.255.255"]

    # Run config commands
    print("Creating loopback510")
    net_connect.send_config_set(config_commands)

    # Run "show ip int brief" to verify
    output = net_connect.send_command("show ip int brief")
    print(output)

    # Always clean up your config!
    print("\nRemoving loopback510")
    cleanup_commands = ["no int loopback510"]
    net_connect.send_config_set(cleanup_commands)

    # Run "show ip int brief" to verify config is removed
    output = net_connect.send_command("show ip int brief")
    print(output)

    # Disconnect from SSH Session
    net_connect.disconnect()


if __name__ == "__main__":
    main()
