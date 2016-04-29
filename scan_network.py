import socket
import sys

def scanning_ip(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, 80))
    
    if result == 0:
        print("IP {}:  Open".format(ip))
        sock.close()
        return 'success'
    else:
        sock.close()
        return 'failed'


for ip1 in range(2,256):
    for ip2 in range(0,256):
        ip = "166.104." + str(ip1) + '.' + str(ip2)
		print('scanning: ' + ip)
		if scanning_ip(ip) == 'success':
			f = open("op.txt", "a")
            f.write(ip + "\n");
            f.close()