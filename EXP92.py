import socket

def mpm():
    host = "127.0.0.1"
    port = 6000
    s = socket.socket()
    s.bind((host, port))
    
    s.listen(1)
    print("Waiting for connection...")

    client, address = s.accept()
    print("Connection Established!")
    print(f"Client Address: {address}")

    while True:
        try:
            print()
            received_data = client.recv(1024)
            decoded_data = received_data.decode("ascii")
            print(f"Client: {decoded_data}")
            print()

            message = input("Enter New Message: ")
            encoded_message = message.encode("ascii")
            client.send(encoded_message)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            break

mpm()
