# AIM: To simulate ARP (IP-to-MAC) and RARP (MAC-to-IP) address resolution.
# ALGORITHM:
# 1. Create a sample ARP table containing IP-to-MAC mappings.
# 2. Build a reverse RARP table from the same mappings.
# 3. For ARP, accept an IP address and search for its MAC address.
# 4. For RARP, accept a MAC address and search for its IP address.
# 5. Display the mapping when found or an explanatory message otherwise.

class ARPRARPSimulator:
    def __init__(self):
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18",
        }
        self.rarp_table = {mac: ip for ip, mac in self.arp_table.items()}

    def arp_request(self, ip_address):
        mac_address = self.arp_table.get(ip_address)
        if mac_address:
            print(f"ARP Reply: {ip_address} is at {mac_address}")
            return mac_address
        print(f"ARP Reply: {ip_address} is not found")
        return None

    def rarp_request(self, mac_address):
        ip_address = self.rarp_table.get(mac_address.lower())
        if ip_address:
            print(f"RARP Reply: {mac_address} is associated with IP {ip_address}")
            return ip_address
        print(f"RARP Reply: {mac_address} is not found")
        return None

    def display_tables(self):
        print("\nARP TABLE (IP -> MAC)")
        for ip_address, mac_address in self.arp_table.items():
            print(f"{ip_address:16} {mac_address}")
        print("\nRARP TABLE (MAC -> IP)")
        for mac_address, ip_address in self.rarp_table.items():
            print(f"{mac_address:20} {ip_address}")


def main():
    simulator = ARPRARPSimulator()
    simulator.display_tables()
    print("\nARP lookup")
    simulator.arp_request(input("Enter IP address: ").strip())
    print("\nRARP lookup")
    simulator.rarp_request(input("Enter MAC address: ").strip())


if __name__ == "__main__":
    main()