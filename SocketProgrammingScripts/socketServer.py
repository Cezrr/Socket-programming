import socket

def serverProgram():
    host = socket.gethostname()
    port = 5000

    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    serverSocket.listen(2)
    conn, address = serverSocket.accept()

    serverSocket.listen(2)
    conn2, address2 = serverSocket.accept()

    print("Connection from: ", str(address))
    print("Connection from: ", str(address2))

    while True:
        data = conn.recv(1024).decode()
        data2 = conn2.recv(1024).decode()
        if not data and not data2:
            break
        print("From connected user: ", address, ":", str(data))
        print("From connected user: ", address2, ":" , str(data2))
        print("for address: ", address, end=" ")
        data = input(" -> ")
        print("for address: ", address2, end=" ")
        data2 = input(" -> ")
        conn.send(data.encode())
        conn2.send(data2.encode())

    conn.close()
    conn2.close()
    
if __name__ == '__main__':
    serverProgram()