1. Find Hostname and IP Address Using Python

import socket

# Get the hostname of the machine

hostname = socket.gethostname()

# Get the IP address associated with the hostname

ip_address = socket.gethostbyname(hostname)

# Display the results

print("Hostname:", hostname)

print("IP Address:", ip_address)

2.Display All IP Addresses of the System

import socket

hostname = socket.gethostname()

# Get all address information

addresses = socket.getaddrinfo(hostname, None)

print("Hostname:", hostname)

print("All IP Addresses:")

ip_list = set()

for addr in addresses:

ip = addr[4][0]

ip_list.add(ip)

for ip in ip_list:

print(ip)

3.Display Public IP Address

import json

import socket

from urllib.request import urlopen

hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

try:

with urlopen("https://api.ipify.org?format=json", timeout=5) as response:

data = json.load(response)

public_ip = data.get("ip", "Unknown")

except Exception as e:

public_ip = f"Unable to fetch public IP: {e}"

print("- Hostname:", hostname)

print("- Local IP:", local_ip)

print("- Public IP:", public_ip)

4. Find Website IP Address

import socket

website = "www.google.com"

ip = socket.gethostbyname(website)

print("Website :", website)

print("IP Address :", ip)

5. DNS Lookup

import socket

host = input("Enter Website: ")

print(socket.gethostbyname_ex(host))

6. Ping

import os

host = input("Enter IP:")

os.system("ping " + host)

7. Find Port Number of a Service

import socket

target = input("Enter IP Address: ")

for port in range(1, 101):

s = socket.socket()

result = s.connect_ex((target, port))

if result == 0:

print("Port", port, "is Open")

s.close()
