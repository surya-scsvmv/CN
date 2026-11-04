# AIM: To identify the machine hostname and its IP addresses using Python.
# ALGORITHM:
# 1. Import the socket module.
# 2. Obtain the local hostname using gethostname().
# 3. Resolve the hostname to its IPv4 address and list available addresses.
# 4. Resolve a user-provided website name when requested.
# 5. Display the hostname and resolved addresses.

import socket


def main():
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    try:
        local_ip = socket.gethostbyname(hostname)
        print("Local IP Address:", local_ip)
    except socket.gaierror as error:
        print("Unable to resolve local hostname:", error)

    print("\nAll available IP addresses:")
    addresses = socket.getaddrinfo(hostname, None)
    unique_addresses = sorted({item[4][0] for item in addresses})
    for address in unique_addresses:
        print(address)

    website = input("\nEnter a website to resolve (or press Enter to skip): ").strip()
    if website:
        try:
            print("Website IP Address:", socket.gethostbyname(website))
        except socket.gaierror as error:
            print("DNS lookup failed:", error)


if __name__ == "__main__":
    main()