# get ip address of the given website

import socket

hostname = input("Please enter your website: ")

# IP lookup from hostname

print(f"The {hostname} IP address is {socket.gethostbyname(hostname)}")