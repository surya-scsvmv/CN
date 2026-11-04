# AIM:
# To write a Python program to identify the machine's host name and IP address.
#
# ALGORITHM:
# 1. Import the socket, os, json, and urllib modules as required.
# 2. Retrieve the local host name and resolve its IP address.
# 3. Display all addresses returned for the local host.
# 4. Resolve a website name and display its IP address.
# 5. Accept a domain name for DNS lookup and display the result.
# 6. Run a ping command for a user-provided host.
# 7. Optionally check TCP ports 1 through 100 on a host you own or are authorized to test.

import json
import os
import socket
from urllib.request import urlopen


def main():
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        local_ip = "Unable to resolve local hostname"

    print("Hostname:", hostname)
    print("IP Address:", local_ip)

    print("\nAll IP Addresses:")
    addresses = socket.getaddrinfo(hostname, None)
    for address in sorted({item[4][0] for item in addresses}):
        print(address)

    print("\nPublic IP Address:")
    try:
        with urlopen("https://api.ipify.org?format=json", timeout=5) as response:
            public_ip = json.load(response).get("ip", "Unknown")
        print(public_ip)
    except Exception as error:
        print("Unable to fetch public IP:", error)

    website = "www.google.com"
    try:
        print("\nWebsite:", website)
        print("Website IP Address:", socket.gethostbyname(website))
    except socket.gaierror as error:
        print("DNS resolution failed:", error)

    domain = input("\nEnter a domain for DNS lookup: ").strip()
    if domain:
        try:
            print("DNS Lookup:", socket.gethostbyname_ex(domain))
        except socket.gaierror as error:
            print("DNS lookup failed:", error)

    target = input("\nEnter a host to ping (or press Enter to skip): ").strip()
    if target:
        os.system(f"ping -n 4 {target}")

    scan_target = input("\nEnter an authorized host for TCP port check (or press Enter to skip): ").strip()
    if scan_target:
        print("Checking TCP ports 1-100 on", scan_target)
        for port in range(1, 101):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(0.2)
                if client.connect_ex((scan_target, port)) == 0:
                    print("Open TCP port:", port)


if __name__ == "__main__":
    main()
