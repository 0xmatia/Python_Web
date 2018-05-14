from scapy3k.all import *

DNS_IP = "8.8.8.8"
DNS_PORT = 53
SRC_PORT = 10212


def main():
    url = input("Enter a domain: ")
    get_response(url)


def get_response(url):
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
    print("IP: " + ans[DNS][DNSRR].rdata)


if __name__ == '__main__':
    main()
