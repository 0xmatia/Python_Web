from scapy.layers.inet import *
from scapy.sendrecv import *
import socket

EXECUTE_FINISH = "YES000finished"  # this is what I got from the server while sending info manually. this should work on the program has well
LOCAL_HOST = "127.0.0.1"
IPA = "54.71.128.194"


def main():
    sniff(lfilter=alien_up, prn=activate_program, count=1)  # we only need one packet to determine that the countdown has started
    print("done")


def alien_up(packet):
    """
    The function checks if the packet is from the alien program
    :param packet: the packet to check
    :type packet: packet
    :return: true if the packet is from the client, false otherwise
    :rtype: bool
    """
    return (IP in packet) and (packet[IP].dst == IPA)


def activate_program(packet):
    """
    The function sends the finish message to the program
    :param packet: the packet to know what is the port
    :type packet: packet
    :return: none
    """
    port = int(packet[UDP].sport)
    con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # open udp socket (can also use scapy but it is easier that way)
    server_address = (LOCAL_HOST, port)
    con.sendto(EXECUTE_FINISH.encode(), server_address)
    con.close()


if __name__ == '__main__':
    main()
