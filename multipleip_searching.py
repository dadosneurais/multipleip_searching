from socket import socket
from IPy import IP 

with open('ips.txt', 'r') as r:
    ipaddresses = r.read().splitlines()

ports = [80, 443, 50, 2049, 21, 22, 23]

with open('results.txt', 'w') as r:
    for ip in ipaddresses:
        try:
            IP(ip)  # test if it's a valided ip
        except ValueError:
            continue

        r.write(f"IP: {ip}\n")

        for port in ports:
            try:
                s = socket()
                s.settimeout(0.5)  # it can compromise the detection port. commend this line if you not hurry
                s.connect((ip, port))
                s.close()
                r.write(f"  Port {port} is open\n")
            except:
                pass

        r.write("\n")
