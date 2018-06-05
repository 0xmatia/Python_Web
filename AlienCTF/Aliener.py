from scapy.layers.inet import *
import socket

NUM_OF_LETTERS = 26
IP_ADDR = "54.71.128.194"
PORT = 99

AIRPORT = "nevada25.84"
TIME = "15:52"
LANE = "earth.jup"
VEHICLE = "2554"


def main():
    print("Running")
    # sniff(lfilter=alien_packet, prn=process_alien)  # i sniffed with scapy and gathered the information for take off. NO NEED FOR THIS ANYMORE
    # send data:
    con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (IP_ADDR, PORT)
    # send the name of the planet
    planet = "ENT003" + cypher("jupiter", 3, 0)
    con.sendto(planet.encode(), server_address)
    server_msg, server_addr = con.recvfrom(1024)
    print(server_msg.decode())  # check for response

    msg = "airport=" + AIRPORT + ",time=" + TIME + ",lane=" + LANE + ",vehicle=" + VEHICLE + ",fly"
    encoded_msg = "FLY008" + cypher(msg, 8, 0)
    print(encoded_msg)
    con.sendto(encoded_msg.encode(), server_address)
    for i in range(2):
        server_msg, server_addr = con.recvfrom(1024)
        print(server_msg.decode())
        print("Decoded- " + cypher(server_msg.decode()[6:], int(server_msg.decode()[3:6]), 1))
    # act like a proxy, and send "finished"          
    con.close()


def cypher(cypher, key, mode):
    """
    The function encrypts / decrypts a cypher
    :param cypher: the cypher to decrypt / encrypt
    :type cypher: str
    :param key: the key to decrypt with
    :type key: int
    :param mode: mode = 1 -decrypt, 0 for encrypt
    :type mode: int
    :return: encrypted / decrypted cypher
    :rtype: str
    """
    new_str = ""
    for item in cypher:
        x = ord(item)
        if item.isalpha():
            if mode == 1:
                x -= key
            else:
                x += key
            if x < ord('a'):
                x += NUM_OF_LETTERS
            if x > ord('z'):
                x -= NUM_OF_LETTERS
        new_str += chr(x)
    return new_str


def alien_packet(packet):
    """
    The function checks if the packet is from the alien server and program
    :param packet: the packet
    :type packet: packet
    :return: true if the packet is valid false other wise
    """
    return (UDP in packet) and (IP in packet) and (packet[IP].src == IP_ADDR or packet[IP].dst == IP_ADDR)


def process_alien(packet):
    """
    the function decrypts the messages from the server and the program.
    :param packet: the packet to process
    :type packet: packet
    :return: Nothing. just prints the data so I can save the details
    """
    info = packet[Raw].load.decode()
    beg = info[0:6]
    print(beg + " - " + info[6:])
    print(beg + " - " + cypher(info[6:], int(info[3:6]), 1))
    print("==========================")


if __name__ == '__main__':
    main()
