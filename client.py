import socket
import select

sock = socket.socket()
sock.connect(('localhost', 6473))
