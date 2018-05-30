from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import *
from scapy.sendrecv import srp1
from datetime import datetime, timedelta

DNS_IP = "8.8.8.8"
DNS_PORT = 53
SRC_PORT = 10212


def main():
    url = input("Enter a domain: ")
    ipmsg = IP(dst=dns_lookup(url))
    icmpmsg = ICMP()
    msg = ipmsg / icmpmsg
    time_list = []
    for i in range(0, 3):
        t = datetime.now()
        sr1(msg, verbose=0)
        print(str(i + 1) + ":   " + str(int((datetime.now() - t).microseconds / 1000)))
        time_list.append(int((datetime.now() - t).microseconds / 1000))
    print("Average ping: ", int((time_list[0]+time_list[1]+time_list[2])/3))


def dns_lookup(url):
    """
    The function sends a dns request to 8.8.8.8 and prints the response
    :param url: the requested url to find
    :type url: str
    :return: None
    :rtype: None
    """
    ethmsg = Ether()
    ipmsg = IP(dst=DNS_IP)
    udpmsg = UDP(sport=SRC_PORT, dport=DNS_PORT)
    dnsmsg = DNS(rd=1, qd=DNSQR(qname=url))
    msg = ethmsg / ipmsg / udpmsg / dnsmsg
    ans = srp1(msg, verbose=0)
    t = datetime.now().microsecond
    return ans[DNS][DNSRR].rdata


if __name__ == '__main__':
    main()
