# AIM:
# To implement a multi-client chat application using TCP sockets.
#
# ALGORITHM:
# 1. Create a TCP chat server on localhost port 55555.
# 2. Accept each client and handle it in a separate thread.
# 3. Broadcast messages received from a client to all other connected clients.
# 4. Create a client that connects to the server and starts a receiving thread.
# 5. Send keyboard messages to the server; enter exit to disconnect.

import socket
import threading


HOST = "127.0.0.1"
PORT = 55555
clients = []
clients_lock = threading.Lock()


def remove_client(client_socket):
    with clients_lock:
        if client_socket in clients:
            clients.remove(client_socket)
    try:
        client_socket.close()
    except OSError:
        pass


def broadcast(message, sender):
    with clients_lock:
        recipients = [client for client in clients if client is not sender]

    for client in recipients:
        try:
            client.sendall(message)
        except OSError:
            remove_client(client)


def handle_client(client_socket, client_address):
    print("New connection from", client_address)
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"{client_address}: {message.decode(errors='replace')}")
            broadcast(message, client_socket)
    except OSError as error:
        print(f"Connection error for {client_address}: {error}")
    finally:
        remove_client(client_socket)
        print(client_address, "disconnected")


def chat_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Chat server listening on {HOST}:{PORT}")
        try:
            while True:
                client_socket, client_address = server_socket.accept()
                with clients_lock:
                    clients.append(client_socket)
                thread = threading.Thread(
                    target=handle_client,
                    args=(client_socket, client_address),
                    daemon=True,
                )
                thread.start()
        except KeyboardInterrupt:
            print("\nChat server stopped.")
        finally:
            with clients_lock:
                active_clients = clients[:]
            for client in active_clients:
                remove_client(client)


def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                print("\nDisconnected from server.")
                break
            print("\n" + message.decode(errors="replace"))
    except OSError:
        pass


def chat_client():
    try:
        with socket.create_connection((HOST, PORT)) as client_socket:
            print("Connected. Type exit to quit.")
            receiver = threading.Thread(
                target=receive_messages,
                args=(client_socket,),
                daemon=True,
            )
            receiver.start()

            while True:
                message = input()
                if message.lower() == "exit":
                    break
                client_socket.sendall(message.encode())
    except OSError as error:
        print("Unable to connect:", error)


if __name__ == "__main__":
    print("1. Start chat server")
    print("2. Start chat client")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        chat_server()
    elif choice == "2":
        chat_client()
    else:
        print("Invalid option.")
