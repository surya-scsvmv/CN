# AIM:
# To write a program to obtain the local DNS server's host name and IP address.
#
# ALGORITHM:
# 1. Import the socket module.
# 2. Obtain the local machine's host name.
# 3. Create a UDP socket and connect it to the configured DNS server address.
# 4. Retrieve the local IP address selected for the connection.
# 5. Close the socket and display the host name and IP address.

import socket


def main():
    hostname = socket.gethostname()
    ip_address = "Unable to determine local IP address"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            connection.connect(("8.8.8.8", 80))
            ip_address = connection.getsockname()[0]
    except OSError as error:
        print("Unable to determine local IP address:", error)

    print("Host Name :", hostname)
    print("IP Address:", ip_address)


if __name__ == "__main__":
    main()
