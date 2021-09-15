import socket

hostname = socket.gethostname()

IpAddress = socket.gethostbyname(hostname)

print(IpAddress)