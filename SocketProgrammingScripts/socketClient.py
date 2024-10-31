import socket

def clientProgram():
    host = socket.gethostname()
    port = 5000

    clientSocket = socket.socket()
    clientSocket.connect((host, port))
    
    message = input(" -> ")

    while message.lower().strip() != "bye":
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()

        print("Recieved from server: ", str(data))
        message = input(" -> ")

    clientSocket.close()

if __name__ == "__main__":
    clientProgram()