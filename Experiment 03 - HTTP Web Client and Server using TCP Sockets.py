# AIM: To download a web page using an HTTP GET request over a TCP socket.
# ALGORITHM:
# 1. Read the target hostname, port, and resource path.
# 2. Create an IPv4 TCP socket and connect to the web server.
# 3. Construct and send a valid HTTP/1.1 GET request.
# 4. Receive the response until the server closes the connection.
# 5. Display the response and close the socket safely.

import socket


def download_web_page(hostname, port=80, path="/"):
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {hostname}\r\n"
        "Connection: close\r\n\r\n"
    )
    response = bytearray()
    with socket.create_connection((hostname, port), timeout=10) as client:
        client.sendall(request.encode("ascii"))
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            response.extend(chunk)
    return bytes(response).decode("utf-8", errors="replace")


def main():
    hostname = input("Enter HTTP website hostname (for example: neverssl.com): ").strip()
    path = input("Enter path (press Enter for /): ").strip() or "/"
    if not hostname:
        raise ValueError("A hostname is required.")
    if not path.startswith("/"):
        path = "/" + path
    print(download_web_page(hostname, 80, path))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        print("Request failed:", error)