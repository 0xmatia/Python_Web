from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import *
from scapy.sendrecv import srp1


def proc(packet):
    if IP in packet:
        print(packet[IP].src + " --> " + packet[IP].dst)


sniff(prn=proc)
