import socket
import struct
import textwrap




def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print(f"Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}")


#Unpack the ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack("!6s6sH", data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]


#Return the adress fromated
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ":".join(bytes_str).uppper()


main()