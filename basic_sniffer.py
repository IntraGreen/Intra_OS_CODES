import socket

# create the sniffer raw socket object
sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket.IPPROTO_ICMP)

# bind it to localhost
sniffer.bind(('0.0.0.0',0))

# make sure that that the IP header is included
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)

print 'sniffer is listening for incoming connections'

# get a single packet
print sniffer.recvfrom(65535)