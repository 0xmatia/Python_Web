from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import *
from scapy.sendrecv import srp1


def filter(packet):
    if ICMP in packet:
        if packet[ICMP].type == 8:
            return True
    return False

def printICMP(packet):
    print("Print replay from " + packet[IP].dst)


sniff(lfilter=filter, prn=printICMP)