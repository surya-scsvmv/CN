# AIM:
# To write a program to obtain the local machine's host name and IP address.
#
# ALGORITHM:
# 1. Import the socket module.
# 2. Obtain the local machine's host name.
# 3. Create a UDP socket.
# 4. Connect the UDP socket to the DNS server address to determine the selected local interface address.
# 5. Read the local IP address using getsockname().
# 6. Close the socket and display the host name and IP address.

import socket


def main():
    hostname = socket.gethostname()
    ip_address = "Unable to determine local IP address"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            connection.connect(("8.8.8.8", 80))
            ip_address = connection.getsockname()[0]
    except OSError as error:
        print("Network lookup failed:", error)

    print("Host Name :", hostname)
    print("IP Address:", ip_address)


if __name__ == "__main__":
    main()
