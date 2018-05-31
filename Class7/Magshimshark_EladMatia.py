from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import *
from scapy.sendrecv import srp1


def main():
    print("Welcome to Magshimshark!\n")
    choice = 1
    while 3 >= choice >= 1:
        print("1 - DNS filter")
        print("2 - Weather filter")
        print("3 - DNS filter")
        print("4 - DNS filter")
        choice = int(input())
        if choice == 1:
            sniff(lfilter=filerDNS, prn=processDNS)
            print("\n\n\n")
        elif choice == 2:
            sniff(lfilter=filter_weather, prn=process_weather)


def filerDNS(packet):
    """
    The function check if the given packet is DNS packet (only answer queries)
    :param packet: the packet to check
    :return: true if the file is a packet, false otherwise
    """
    return DNS in packet and packet[DNS].an is not None


def processDNS(packet):
    """
    The function prints the address returned from the dns query
    :param packet: the packet to check
    :return:
    :rtype: None
    """
    num_of_answers = packet[DNS].ancount
    print(str(packet[DNS].an[num_of_answers-1].rdata))


def filter_weather(packet):
    """
    The function checks if the packets sniffed are weather packers
    :param packet: the packet to check
    :type packet: packet
    :return: True if the packet is a weather packet, false otherwise
    :rtype: bool
    """
    # print(packet.show())
    return IP in packet and packet[IP].src == "52.89.157.137" and Raw in packet and "200:ANSWER" in packet[Raw].load.decode()


def process_weather(packet):
    info = packet[Raw].load.decode()
    result = info[info.find("=")+1:info.find("&city")] + ": " + info[info.find("&text") + len("&text") + 1:]+", " + info[info.find("=", 40)+1:info.find("&text")] + " degrees in " + info[info.find("&city") + len("&city") + 1: info.find("&temp")]
    print(result)


if __name__ == '__main__':
    main()