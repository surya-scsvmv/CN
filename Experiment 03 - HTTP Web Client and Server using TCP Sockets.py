# AIM:
# To write an HTTP web client program to download a webpage using TCP sockets.
#
# ALGORITHM:
# 1. Create an IPv4 TCP socket.
# 2. Connect the socket to the web server on TCP port 80.
# 3. Construct and send an HTTP GET request with the Host and Connection headers.
# 4. Receive response bytes until the server closes the connection.
# 5. Decode and display the HTTP response, then close the socket.

import socket


def download_web_page(hostname, port=80, path="/"):
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {hostname}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    with socket.create_connection((hostname, port), timeout=10) as client_socket:
        client_socket.sendall(request.encode("ascii"))
        response = bytearray()

        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response.extend(data)

    return response.decode("utf-8", errors="replace")


if __name__ == "__main__":
    hostname = input("Enter HTTP website hostname (default: example.com): ").strip()
    hostname = hostname or "example.com"
    try:
        print(download_web_page(hostname))
    except OSError as error:
        print("Unable to download the webpage:", error)
