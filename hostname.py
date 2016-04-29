import socket

with open("ip.txt") as f:
	for line in f:
		ipaddr = line.rstrip("\n")
		hname = socket.getfqdn(line)
		fw = open("output.txt", "a")
		if ipaddr == hname:
			fw.write(ipaddr + "\n")
		else:
			fw.write(ipaddr + " " + hname + "\n")
		fw.close()