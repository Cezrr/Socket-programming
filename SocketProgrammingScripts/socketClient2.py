import socket

def clientProgram2():
    host = socket.gethostname()
    port = 5000

    clientSocket = socket.socket()
    clientSocket.connect((host, port))
    
    message = input(" -> ")

    while message.lower().strip() != "bye":
        clientSocket.send(message.encode())
        data2 = clientSocket.recv(1024).decode()

        print("Recieved from server: ", str(data2))
        message = input(" -> ")

    clientSocket.close()

if __name__ == "__main__":
    clientProgram2()