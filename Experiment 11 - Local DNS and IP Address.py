# AIM: To obtain the local machine hostname and the local IP address used for networking.
# ALGORITHM:
# 1. Import the socket module.
# 2. Obtain the local hostname.
# 3. Create a UDP socket and connect it to a public DNS address to determine the
#    local outbound interface address; no application payload is sent.
# 4. Close the socket and display the hostname and local IP address.

import socket


def main():
    hostname = socket.gethostname()
    ip_address = "Unavailable"
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            connection.connect(("8.8.8.8", 80))
            ip_address = connection.getsockname()[0]
    except OSError as error:
        print("Unable to determine the active interface address:", error)
    print("Host Name:", hostname)
    print("IP Address:", ip_address)


if __name__ == "__main__":
    main()