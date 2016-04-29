import socket


ip_a = "166.104.251.118"
ip_c = "166.104.177.24"
a = socket.getfqdn("166.104.251.118")
b = socket.getfqdn("166.104.99.32")
c = socket.getfqdn("166.104.177.24")

if ip_c == c:
	fw = open("zz.txt", "a")
	fw.write(ip_c + "   " + c + "\n")
else:
	print ip_c + " " + c
	fw = open("zz.txt", "a")
	fw.write(ip_c + "   " + c + "\n")