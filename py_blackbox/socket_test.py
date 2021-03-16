import socket
import time
import struct
from collections import namedtuple

format_ = "iii"
handshake = namedtuple("handshake", "identifier version operationId")
tuple_to_send = handshake(identifier=1,
                          version=1,
                          operationId=0)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    HOST = "127.0.0.1"
    PORT = 9996
    s.connect((HOST, PORT))
    string_to_send = struct.pack(format_, *tuple_to_send._asdict().values())

    s.sendall(string_to_send)
    data = s.recv(1024)
