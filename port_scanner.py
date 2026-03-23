import socket
import re

ip_add_pattern = re.compile('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

port_range_pattern = re.compile('([0-9]+)-([0-9]+)')

port_min = 0
port_max = 65535

print(r""" 
███████╗██╗      █████╗ ███████╗██╗  ██╗     ██████╗ ███████╗    ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝██║     ██╔══██╗██╔════╝██║  ██║    ██╔═══██╗██╔════╝    ██║     ██║██╔════╝ ██║  ██║╚══██╔══╝
█████╗  ██║     ███████║███████╗███████║    ██║   ██║█████╗      ██║     ██║██║  ███╗███████║   ██║   
██╔══╝  ██║     ██╔══██║╚════██║██╔══██║    ██║   ██║██╔══╝      ██║     ██║██║   ██║██╔══██║   ██║   
██║     ███████╗██║  ██║███████║██║  ██║    ╚██████╔╝██║         ███████╗██║╚██████╔╝██║  ██║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝         ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                                                      """)
print("\n*******************************************************************************************")
print("\n Copyright of Stevan Glavaski, 2026.")
print("\n https://stivsworld.infinityfree.me")
print("\n Part of my cybersecurity and python journey.")
print("\n*******************************************************************************************")


open_port = []

while True:
    ip_add_entered = input("Please enter your desired IP address for the port scanner to check: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid IP address")
        break

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (example 60-120)")
    port_range = input("Please enter your desired port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace("",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_port.append(port)

    except:
        pass

for port in open_port:
    print(f"Port {port} is open on {ip_add_entered}.")