from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import *
from scapy.sendrecv import srp1


def main():
    print("Welcome to Magshimshark!")
    print("1 - DNS filter")
    print("2 - DNS filter")
    print("3 - DNS filter")
    choice = int(input())
    if choice == 1:
        try:
            sniff(lfilter=filerDNS, prn=processDNS)
        except Exception:
            print("Hey")


def filerDNS(packet):
    """
    The function check if the given packet is DNS packet
    :param packet: the packet to check
    :return: true if the file is a packet, false otherwise
    """
    return DNS in packet


def processDNS(packet):
    """
    The function prints the address returned from the dns query
    :param packet: the packet to check
    :return:
    :rtype: None
    """
    print(packet[DNS][DNSQR].qname.decode())


if __name__ == '__main__':
    main()