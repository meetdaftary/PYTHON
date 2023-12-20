import socket

def mpm():
    host = "127.0.0.1"
    port = 6000
    s = socket.socket()
    s.connect((host, port))
    
    print("Connection Established!")

    while True:
        try:
            print()
            message = input("Enter New Message: ")
            encoded_message = message.encode("ascii")
            s.send(encoded_message)
            print()

            received_data = s.recv(1024)
            decoded_data = received_data.decode("ascii")
            print(f"Server: {decoded_data}")
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            termination_message = "Connection from Client terminated!".encode("ascii")
            s.send(termination_message)
            break

mpm()
