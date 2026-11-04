# Computer Networks Laboratory

A complete collection of **19 Computer Networks laboratory experiments** covering Windows network commands, packet capture and analysis, Python socket programming, ARP/RARP, CRC error detection, NS-2 simulations, Wireshark analysis, Cisco Packet Tracer, and physical LAN topology study.

## Experiment index

| No. | Experiment | File |
|---:|---|---|
| **01** | Windows network commands and packet analysis | [Experiment 01](<Experiment 01 - Network Commands and Packet Analysis.txt>) |
| **02** | Machine hostname and IP address using Python | [Experiment 02](<Experiment 02 - Machine Hostname and IP Address.py>) |
| **03** | HTTP web client using TCP sockets | [Experiment 03](<Experiment 03 - HTTP Web Client and Server using TCP Sockets.py>) |
| **04** | TCP echo client and server | [Experiment 04](<Experiment 04 - TCP Echo Client and Server.py>) |
| **05** | Multi-client TCP chat application | [Experiment 05](<Experiment 05 - TCP Multi-Client Chat Application.py>) |
| **06** | TCP file transfer | [Experiment 06](<Experiment 06 - TCP File Transfer.py>) |
| **07** | ARP and RARP protocol simulation | [Experiment 07](<Experiment 07 - ARP and RARP Protocol.py>) |
| **08** | TCP and UDP simulation using NS-2 | [Experiment 08](<Experiment 08 - TCP and UDP Simulation using NS2.tcl>) |
| **09** | Distance Vector routing using NS-2 | [Experiment 09](<Experiment 09 - Distance Vector Routing using NS2.tcl>) |
| **10** | Link State routing using NS-2 | [Experiment 10](<Experiment 10 - Link State Routing using NS2.tcl>) |
| **11** | Local hostname and IP address discovery | [Experiment 11](<Experiment 11 - Local DNS and IP Address.py>) |
| **12** | CRC error detection | [Experiment 12](<Experiment 12 - CRC Error Detection.py>) |
| **13** | Wireshark packet capture and inspection | [Experiment 13](<Experiment 13 - Wireshark Packet Capture and Inspection.txt>) |
| **14** | Network packet analysis and Wireshark filters | [Experiment 14](<Experiment 14 - Network Packet Analysis and Wireshark Filters.txt>) |
| **15** | Wireshark filter expressions for packet capture | [Experiment 15](<Experiment 15 - Wireshark Filter Expressions for Packet Capture.txt>) |
| **16** | RTP packet delay and loss analysis using Wireshark | [Experiment 16](<Experiment 16 - RTP Packet Delay and Loss Analysis using Wireshark.txt>) |
| **17** | Inspect network packets using Wireshark | [Experiment 17](<Experiment 17 - Inspect Network Packets using Wireshark.txt>) |
| **18** | Simple LAN using Cisco Packet Tracer | [Experiment 18](<Experiment 18 - Simple LAN using Cisco Packet Tracer.txt>) |
| **19** | Network topologies using Benchmark LAN Trainer Kit | [Experiment 19](<Experiment 19 - Network Topologies using Benchmark LAN Trainer Kit.txt>) |

## Windows setup

Install Git for Windows and Python 3.9+. During Python installation, enable **Add Python to PATH**. Open PowerShell and verify `py --version`.

Clone the repository:

```powershell
git clone https://github.com/surya-scsvmv/CN.git
cd CN
```

Python programs use the standard library; no external packages are required. Run standalone Python experiments using the `py` launcher and quote filenames because they contain spaces:

```powershell
py "Experiment 02 - Machine Hostname and IP Address.py"
py "Experiment 07 - ARP and RARP Protocol.py"
py "Experiment 11 - Local DNS and IP Address.py"
py "Experiment 12 - CRC Error Detection.py"
```

### TCP client/server programs (Experiments 04–06)

Open two or more PowerShell windows in the repository folder. Run the same experiment file in each window. In one window enter `s` to start the server; in the other enter `c` to start a client. For Experiment 05, start the server in one terminal and one or more clients in separate terminals. Experiment 06 asks the client for a file path and saves the received file with a `received_` prefix in the server's working directory. These examples bind to `127.0.0.1` and are designed for local tests. Do not expose the demonstration servers to untrusted networks.

### HTTP TCP client (Experiment 03)

```powershell
py "Experiment 03 - HTTP Web Client and Server using TCP Sockets.py"
```

Enter a hostname that supports plain HTTP on port 80 (for example `neverssl.com`) and a path such as `/`. This example does not implement HTTPS/TLS.

### Windows network commands (Experiment 01)

Run these in Command Prompt or PowerShell:

```powershell
ipconfig /all
netstat -ano
route print
nslookup www.google.com
tracert www.google.com
ping -n 4 www.google.com
getmac /v
arp -a
tasklist
```

For packet capture, install Wireshark with Npcap, launch it as administrator, and select the active Wi-Fi/Ethernet interface. Use display filters such as `icmp`, `dns`, `tcp`, `udp`, or `rtp`. Capture only traffic you are authorised to inspect.

Pktmon is a Windows packet-capture alternative (run an elevated terminal):

```powershell
pktmon start --capture --pkt-size 0
ping -n 4 8.8.8.8
pktmon stop
pktmon etl2pcap PktMon.etl --out packetcapture.pcapng
```

Open the resulting `.pcapng` file in Wireshark. Use `pktmon help` if options differ on your Windows build.

### NS-2 scripts (Experiments 08–10)

NS-2 is not natively bundled with Windows. Use an Ubuntu environment or WSL2 with a compatible NS-2 and NAM installation. NAM needs a working Linux GUI environment (such as WSLg where supported). From the repository folder in that Linux environment, run:

```bash
ns "Experiment 08 - TCP and UDP Simulation using NS2.tcl"
ns "Experiment 09 - Distance Vector Routing using NS2.tcl"
ns "Experiment 10 - Link State Routing using NS2.tcl"
```

Experiments 08–09 create `out.nam`; Experiment 09 also creates `trace.tr`. Experiment 10 creates `link_state.nam` and `link_state.tr`. The scripts invoke NAM at completion. To open the animation manually use `nam out.nam` or `nam link_state.nam`.

### Cisco Packet Tracer (Experiment 18)

Install Cisco Packet Tracer for Windows. Add one 2960 switch and three PCs, connect each PC FastEthernet0 to a switch port with Copper Straight-Through cable, then configure:

| PC | IP address | Subnet mask |
|---|---|---|
| PC0 | 192.168.1.1 | 255.255.255.0 |
| PC1 | 192.168.1.2 | 255.255.255.0 |
| PC2 | 192.168.1.3 | 255.255.255.0 |

From each PC's Desktop > Command Prompt, test with `ping 192.168.1.2` and `ping 192.168.1.3`. Save the project as `.pkt`.

### Benchmark LAN Trainer Kit (Experiment 19)

This is a physical lab exercise, not a Windows program. Use the LAN Trainer Kit, node modules, hub/switch module, patch cords, power supply, and indicator panel to construct and observe bus, star, ring, and mesh topologies. Arrange tree/hybrid layouts only where the supplied modules support them.

## Notes

- Python source files (Experiments 02–07 and 11–12) start with AIM and ALGORITHM comment blocks; implementation comments have been removed.
- Experiments 01 and 13–19 are command-, tool-, or hardware-based lab records, not standalone Python programs.
- Wireshark may require administrator privileges and Npcap.
- The RTP values in Experiment 16 are sample observations; record values from your own capture.
- Experiment 19 depends on the physical trainer kit available in the lab.

## Academic context

Computer Networks Laboratory — Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya (SCSVMV University).
