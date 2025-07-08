import socket
from scapy.all import *
from scapy.layers.l2 import Ether
sniffer_socket=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3)) 
#AF_PACKET specifies address of family within the packet hence used to capture packets at the link layer
#SOCK_RAW used to grab raw data from lower layers of OSI model eg-IP
#ntohs is used to convert numeric 16bit positive integers from network byte into host byte
interface='wlan0'
sniffer_socket.bind((interface,0))
try:
    while True:
        raw_data,addr=sniffer_socket.recvfrom(65535)
        #for checking on all ports-65535,for checking only for HTTP-80
        packet=Ether(raw_data)
        print(packet.summary())
except KeyboardInterrupt:
    sniffer_socket.close()