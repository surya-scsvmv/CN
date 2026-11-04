# AIM:
# To simulate Address Resolution Protocol (ARP) and Reverse Address Resolution Protocol (RARP).
#
# ALGORITHM:
# 1. Create an IP-to-MAC address mapping table.
# 2. Build a reverse MAC-to-IP mapping table.
# 3. For ARP, accept an IP address and display its mapped MAC address.
# 4. For RARP, accept a MAC address and display its mapped IP address.
# 5. Display the tables and demonstrate successful and unsuccessful lookups.

class ARP_RARP_Simulator:
    def __init__(self):
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18",
        }
        self.rarp_table = {
            mac: ip for ip, mac in self.arp_table.items()
        }

    def arp_request(self, ip_address):
        print(f"ARP Request: Who has {ip_address}?")
        mac_address = self.arp_table.get(ip_address)
        if mac_address:
            print(f"ARP Reply: {ip_address} is at {mac_address}.")
            return mac_address
        print(f"ARP Reply: {ip_address} is not found.")
        return None

    def rarp_request(self, mac_address):
        print(f"RARP Request: Who has MAC address {mac_address}?")
        ip_address = self.rarp_table.get(mac_address.lower())
        if ip_address:
            print(f"RARP Reply: {mac_address} is associated with IP {ip_address}.")
            return ip_address
        print(f"RARP Reply: {mac_address} is not found.")
        return None

    def display_tables(self):
        print("\nARP TABLE")
        print("IP Address\t\tMAC Address")
        for ip, mac in self.arp_table.items():
            print(f"{ip}\t{mac}")

        print("\nRARP TABLE")
        print("MAC Address\t\t\tIP Address")
        for mac, ip in self.rarp_table.items():
            print(f"{mac}\t{ip}")

    def add_entry(self, ip_address, mac_address):
        self.arp_table[ip_address] = mac_address.lower()
        self.rarp_table[mac_address.lower()] = ip_address
        print("Entry added successfully.")


if __name__ == "__main__":
    simulator = ARP_RARP_Simulator()
    simulator.display_tables()

    print("\nARP EXAMPLES")
    simulator.arp_request("192.168.1.1")
    simulator.arp_request("192.168.1.100")

    print("\nRARP EXAMPLES")
    simulator.rarp_request("00:0a:95:9d:68:16")
    simulator.rarp_request("00:0a:95:9d:68:99")

    print("\nADD NEW ENTRY")
    simulator.add_entry("192.168.1.4", "00:0a:95:9d:68:19")
    simulator.display_tables()
