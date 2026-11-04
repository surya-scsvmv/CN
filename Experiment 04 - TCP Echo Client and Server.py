# AIM: To implement an echo server and client using TCP sockets.
# ALGORITHM:
# Server: create a TCP socket, bind to a port, listen, and accept a client.
# Receive each message and send the same bytes back until the client disconnects.
# Client: connect to the server, read messages, send them, and display echoed replies.
# Type exit to close the client connection; stop the server with Ctrl+C.

import socket

HOST = "127.0.0.1"
PORT = 65432


def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Echo server listening on {HOST}:{PORT}")
        try:
            while True:
                connection, address = server.accept()
                with connection:
                    print("Connected:", address)
                    while True:
                        data = connection.recv(1024)
                        if not data:
                            break
                        print("Received:", data.decode(errors="replace"))
                        connection.sendall(data)
        except KeyboardInterrupt:
            print("\nServer stopped.")


def echo_client():
    with socket.create_connection((HOST, PORT), timeout=10) as client:
        print("Connected to echo server. Type exit to quit.")
        while True:
            message = input("You: ")
            client.sendall(message.encode())
            reply = client.recv(1024)
            if not reply:
                print("Server disconnected.")
                break
            print("Echo:", reply.decode(errors="replace"))
            if message.lower() == "exit":
                break


if __name__ == "__main__":
    role = input("Run as server or client? [s/c]: ").strip().lower()
    try:
        if role == "s":
            echo_server()
        elif role == "c":
            echo_client()
        else:
            print("Enter s for server or c for client.")
    except OSError as error:
        print("Network error:", error)