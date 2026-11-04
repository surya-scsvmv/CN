# AIM: To transfer a file from a TCP client to a TCP server.
# ALGORITHM:
# Server: bind and listen for a client, receive a length-prefixed filename and file size,
# then receive exactly that number of bytes and save the file with a received_ prefix.
# Client: connect to the server, select an existing file, and send its name, size, and bytes.
# Both sides close their sockets and file handles after transfer.

import os
import socket
import struct

HOST = "127.0.0.1"
PORT = 12345
CHUNK_SIZE = 4096


def receive_exact(connection, size):
    data = bytearray()
    while len(data) < size:
        chunk = connection.recv(min(CHUNK_SIZE, size - len(data)))
        if not chunk:
            raise ConnectionError("Connection closed before the complete file was received.")
        data.extend(chunk)
    return bytes(data)


def file_transfer_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"File server listening on {HOST}:{PORT}")
        connection, address = server.accept()
        with connection:
            print("Connected:", address)
            name_length = struct.unpack("!H", receive_exact(connection, 2))[0]
            filename = receive_exact(connection, name_length).decode("utf-8")
            file_size = struct.unpack("!Q", receive_exact(connection, 8))[0]
            safe_name = os.path.basename(filename)
            if not safe_name or safe_name in {".", ".."}:
                raise ValueError("Invalid filename received.")
            output_name = "received_" + safe_name
            remaining = file_size
            with open(output_name, "wb") as output:
                while remaining:
                    chunk = connection.recv(min(CHUNK_SIZE, remaining))
                    if not chunk:
                        raise ConnectionError("Connection closed during transfer.")
                    output.write(chunk)
                    remaining -= len(chunk)
            print(f"Received {file_size} bytes and saved as {output_name}")


def file_transfer_client():
    filename = input("Enter the path of the file to send: ").strip().strip('"')
    if not os.path.isfile(filename):
        raise FileNotFoundError(filename)
    name = os.path.basename(filename).encode("utf-8")
    if len(name) > 65535:
        raise ValueError("Filename is too long.")
    file_size = os.path.getsize(filename)
    with socket.create_connection((HOST, PORT), timeout=10) as client:
        client.sendall(struct.pack("!H", len(name)) + name + struct.pack("!Q", file_size))
        with open(filename, "rb") as source:
            while True:
                chunk = source.read(CHUNK_SIZE)
                if not chunk:
                    break
                client.sendall(chunk)
    print(f"File {filename} ({file_size} bytes) sent successfully.")


if __name__ == "__main__":
    role = input("Run as server or client? [s/c]: ").strip().lower()
    try:
        if role == "s":
            file_transfer_server()
        elif role == "c":
            file_transfer_client()
        else:
            print("Enter s for server or c for client.")
    except (OSError, ValueError, ConnectionError) as error:
        print("Transfer failed:", error)