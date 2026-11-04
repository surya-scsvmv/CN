# AIM: To implement a multi-client chat application using TCP sockets and threads.
# ALGORITHM:
# Server: listen on a TCP port and accept each new client in a separate thread.
# Receive messages from each client and broadcast them to the other connected clients.
# Remove a client from the list when its connection closes.
# Client: connect to the server, run a receiver thread, and send typed messages.
# Type exit to disconnect a client; stop the server with Ctrl+C.

import socket
import threading

HOST = "127.0.0.1"
PORT = 55555
clients = set()
clients_lock = threading.Lock()


def broadcast(message, sender):
    failed = []
    with clients_lock:
        recipients = list(clients)
    for client in recipients:
        if client is sender:
            continue
        try:
            client.sendall(message)
        except OSError:
            failed.append(client)
    if failed:
        with clients_lock:
            for client in failed:
                clients.discard(client)


def handle_client(connection, address):
    print(f"Connected: {address}")
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            message = data.decode(errors="replace").strip()
            print(f"{address}: {message}")
            if message.lower() == "exit":
                break
            broadcast(f"{address}: {message}".encode(), connection)
    except OSError as error:
        print(f"Connection error for {address}: {error}")
    finally:
        with clients_lock:
            clients.discard(connection)
        connection.close()
        print(f"Disconnected: {address}")


def chat_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(10)
        print(f"Chat server listening on {HOST}:{PORT}")
        try:
            while True:
                connection, address = server.accept()
                with clients_lock:
                    clients.add(connection)
                threading.Thread(target=handle_client, args=(connection, address), daemon=True).start()
        except KeyboardInterrupt:
            print("\nChat server stopped.")


def receive_messages(client):
    try:
        while True:
            data = client.recv(1024)
            if not data:
                print("\nDisconnected from server.")
                break
            print("\n" + data.decode(errors="replace") + "\nYou: ", end="", flush=True)
    except OSError:
        pass


def chat_client():
    with socket.create_connection((HOST, PORT), timeout=10) as client:
        print("Connected. Open another terminal and run another client to chat. Type exit to quit.")
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
        while True:
            message = input("You: ")
            client.sendall(message.encode())
            if message.lower() == "exit":
                break


if __name__ == "__main__":
    role = input("Run as server or client? [s/c]: ").strip().lower()
    try:
        if role == "s":
            chat_server()
        elif role == "c":
            chat_client()
        else:
            print("Enter s for server or c for client.")
    except OSError as error:
        print("Network error:", error)