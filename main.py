import sys
import socket
import select

server = socket.socket()    
server.bind(('localhost', 6473))            #создание сервера

clients = []

server.listen(5)
conn, addr = server.accept()
    
sockets = [sys.stdin, server] + clients
read_sockets, write_sockets, error_sockets = select.select(sockets, [], [], 0)
for i in ins:
    if i is server:
        conn, addr = server.accept()
        clients.append(conn)
    else:
        data = conn.recv(4)                         
        if not data:                                #check connection
            conn.close()
            conn.send(b'Hello, World!')
