# sudo apt-get install python3-pip
#pip3 install IPy


import socket
from IPy import IP


def check_ip(ip):
    try:
       IP(ip) #filter ip
       return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ip_address,port):
    try:     
       sock = socket.socket()
       sock.connect((ip_address, port))
       sock.settimeout(0.5)
       print(f"port {port} is opened")
    except:
        return 0

#getting inputs
ip_address =input('|....Enter target to scan : ')         
pr=int(input("|....Enter ports range : "))
print("\n")

#call to funcs
filtered_ip = check_ip(ip_address)

for port in range(0,pr):
    scan_port(filtered_ip,port)