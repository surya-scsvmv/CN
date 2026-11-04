# AIM:
# To implement TCP socket communication using an echo client and echo server.
#
# ALGORITHM:
# 1. Create a TCP server socket, bind it to localhost port 65432, and listen.
# 2. Accept a client connection.
# 3. Receive client data and send the same data back.
# 4. The client connects to the server, sends messages, and prints echoed replies.
# 5. Enter exit to close the client; stop the server with Ctrl+C.

import socket


HOST = "127.0.0.1"
PORT = 65432


def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Echo server listening on {HOST}:{PORT}")

        try:
            while True:
                connection, address = server_socket.accept()
                with connection:
                    print("Connected by", address)
                    while True:
                        data = connection.recv(1024)
                        if not data:
                            break
                        print("Received:", data.decode(errors="replace"))
                        connection.sendall(data)
                    print("Client disconnected.")
        except KeyboardInterrupt:
            print("\nServer stopped.")


def echo_client():
    try:
        with socket.create_connection((HOST, PORT)) as client_socket:
            while True:
                message = input("Enter a message (exit to quit): ")
                client_socket.sendall(message.encode())
                if message.lower() == "exit":
                    break
                response = client_socket.recv(1024)
                if not response:
                    print("Server disconnected.")
                    break
                print("Echoed from server:", response.decode(errors="replace"))
    except OSError as error:
        print("Client error:", error)


if __name__ == "__main__":
    print("1. Start server")
    print("2. Start client")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        echo_server()
    elif choice == "2":
        echo_client()
    else:
        print("Invalid option.")
