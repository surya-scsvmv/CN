# AIM:
# To implement file transfer between a TCP client and server.
#
# ALGORITHM:
# 1. Start a TCP server on localhost port 12345.
# 2. Accept a client, receive the file name and file size.
# 3. Receive exactly the declared number of bytes and save them in a destination file.
# 4. The client connects to the server and checks that the source file exists.
# 5. The client sends the file name, size, and file data in chunks.
# 6. Close the connection after the transfer is complete.

import os
import socket
import struct


HOST = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 4096


def receive_exact(connection, size):
    data = bytearray()
    while len(data) < size:
        chunk = connection.recv(min(BUFFER_SIZE, size - len(data)))
        if not chunk:
            raise ConnectionError("Connection closed before transfer completed.")
        data.extend(chunk)
    return bytes(data)


def file_transfer_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"File server listening on {HOST}:{PORT}")

        connection, address = server_socket.accept()
        with connection:
            print("Connected by", address)
            name_length = struct.unpack("!H", receive_exact(connection, 2))[0]
            filename = receive_exact(connection, name_length).decode("utf-8")
            file_size = struct.unpack("!Q", receive_exact(connection, 8))[0]
            safe_name = os.path.basename(filename)
            destination = f"received_{safe_name}"

            with open(destination, "wb") as output_file:
                remaining = file_size
                while remaining:
                    chunk = connection.recv(min(BUFFER_SIZE, remaining))
                    if not chunk:
                        raise ConnectionError("Connection lost during file transfer.")
                    output_file.write(chunk)
                    remaining -= len(chunk)

            connection.sendall(b"OK")
            print(f"File received and saved as {destination}")


def file_transfer_client():
    filename = input("Enter the file path to send: ").strip().strip('"')
    if not os.path.isfile(filename):
        print("File not found.")
        return

    file_size = os.path.getsize(filename)
    file_name = os.path.basename(filename).encode("utf-8")
    if len(file_name) > 65535:
        print("File name is too long.")
        return

    try:
        with socket.create_connection((HOST, PORT), timeout=10) as client_socket:
            client_socket.sendall(struct.pack("!H", len(file_name)))
            client_socket.sendall(file_name)
            client_socket.sendall(struct.pack("!Q", file_size))

            with open(filename, "rb") as input_file:
                while True:
                    chunk = input_file.read(BUFFER_SIZE)
                    if not chunk:
                        break
                    client_socket.sendall(chunk)

            acknowledgement = client_socket.recv(2)
            if acknowledgement == b"OK":
                print(f"File '{filename}' sent successfully.")
            else:
                print("Server did not confirm the transfer.")
    except OSError as error:
        print("File transfer failed:", error)


if __name__ == "__main__":
    print("1. Start file server")
    print("2. Start file client")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        file_transfer_server()
    elif choice == "2":
        file_transfer_client()
    else:
        print("Invalid option.")
