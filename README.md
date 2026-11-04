# Computer Networks Laboratory

A structured collection of **19 Computer Networks (CN) laboratory experiments**, following the SCSVMV Computer Networks Lab Manual for Academic Year 2026–27. The repository includes Windows network commands, Python socket programs, NS-2 simulations, Wireshark analysis, Cisco Packet Tracer, and hands-on LAN topology study.

<p>
  <img src="https://img.shields.io/badge/Focus-Computer%20Networks-2563EB?style=flat-square" alt="Computer Networks"/>
  <img src="https://img.shields.io/badge/Python-Socket%20Programming-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python socket programming"/>
  <img src="https://img.shields.io/badge/Simulator-NS--2-0F766E?style=flat-square" alt="NS-2"/>
  <img src="https://img.shields.io/badge/Experiments-19-7C3AED?style=flat-square" alt="19 experiments"/>
</p>

## Experiment index

| No. | Experiment | File |
|---:|---|---|
| **01** | Network commands and packet analysis | [Experiment 01](<Experiment 01 - Network Commands and Packet Analysis.txt>) |
| **02** | Machine hostname and IP address using Python | [Experiment 02](<Experiment 02 - Machine Hostname and IP Address.py>) |
| **03** | HTTP web client using TCP sockets | [Experiment 03](<Experiment 03 - HTTP Web Client and Server using TCP Sockets.py>) |
| **04** | TCP echo client and server | [Experiment 04](<Experiment 04 - TCP Echo Client and Server.py>) |
| **05** | Multi-client TCP chat application | [Experiment 05](<Experiment 05 - TCP Multi-Client Chat Application.py>) |
| **06** | TCP file transfer | [Experiment 06](<Experiment 06 - TCP File Transfer.py>) |
| **07** | ARP and RARP protocol simulation | [Experiment 07](<Experiment 07 - ARP and RARP Protocol.py>) |
| **08** | TCP and UDP performance simulation using NS-2 | [Experiment 08](<Experiment 08 - TCP and UDP Simulation using NS2.tcl>) |
| **09** | Distance Vector routing simulation using NS-2 | [Experiment 09](<Experiment 09 - Distance Vector Routing using NS2.tcl>) |
| **10** | Link State routing simulation using NS-2 | [Experiment 10](<Experiment 10 - Link State Routing using NS2.tcl>) |
| **11** | Local DNS server hostname and IP address | [Experiment 11](<Experiment 11 - Local DNS and IP Address.py>) |
| **12** | Link State routing simulation using NS-2 | [Experiment 12](<Experiment 12 - Link State Routing using NS2.tcl>) |
| **13** | Local DNS server hostname and IP address | [Experiment 13](<Experiment 13 - Local DNS Server Hostname and IP Address.py>) |
| **14** | Cyclic Redundancy Check (CRC) | [Experiment 14](<Experiment 14 - Cyclic Redundancy Check CRC.py>) |
| **15** | Wireshark filter expressions for packet capture | [Experiment 15](<Experiment 15 - Wireshark Filter Expressions.txt>) |
| **16** | RTP packet delay and loss analysis using Wireshark | [Experiment 16](<Experiment 16 - RTP Packet Delay and Loss Analysis using Wireshark.txt>) |
| **17** | Inspect packets on your network using Wireshark | [Experiment 17](<Experiment 17 - Inspect Network Packets using Wireshark.txt>) |
| **18** | Simple LAN using Cisco Packet Tracer | [Experiment 18](<Experiment 18 - Simple LAN using Cisco Packet Tracer.txt>) |
| **19** | Network topologies using Benchmark LAN Trainer Kit | [Experiment 19](<Experiment 19 - Network Topologies using Benchmark LAN Trainer Kit.txt>) |

## Requirements

Install only the tools needed for the experiment you are performing.

| Tool | Experiments | Purpose |
|---|---|---|
| **Windows 10/11** | 01–07, 11, 13–18 | Command Prompt, PowerShell, Python, and GUI applications |
| **Python 3.10+** | 02–07, 11, 13–14 | Host/DNS lookup, TCP sockets, ARP/RARP simulation, CRC |
| **NS-2 and NAM** | 08–10, 12 | Network simulation and animation |
| **Wireshark + Npcap** | 01, 15–17 | Packet capture and protocol analysis |
| **Cisco Packet Tracer 8.x** | 18 | LAN design and connectivity simulation |
| **Benchmark LAN Trainer Kit** | 19 | Physical topology construction and observation |

## Windows setup

### 1. Clone the repository

Open **Command Prompt** or **PowerShell**:

```powershell
git clone https://github.com/surya-scsvmv/CN.git
cd CN
```

### 2. Install and verify Python

Install Python 3 from [python.org](https://www.python.org/downloads/windows/). During installation, enable **Add Python to PATH**.

Verify:

```powershell
py --version
```

The Python experiments use the standard library; no `pip install` is required.

Run a Python file from the repository folder:

```powershell
py "Experiment 02 - Machine Hostname and IP Address.py"
py "Experiment 03 - HTTP Web Client and Server using TCP Sockets.py"
py "Experiment 07 - ARP and RARP Protocol.py"
py "Experiment 11 - Local DNS and IP Address.py"
py "Experiment 13 - Local DNS Server Hostname and IP Address.py"
py "Experiment 14 - Cyclic Redundancy Check CRC.py"
```

You may also use `python` instead of `py` when the Python launcher is not available.

## Running each type of experiment on Windows

### Experiment 01 — Windows network commands and packet analysis

Open **Command Prompt** or **PowerShell**. Run commands individually:

```powershell
ipconfig /all
ping -n 4 8.8.8.8
netstat -ano
nslookup google.com
tracert -d 8.8.8.8
```

For packet capture using Windows Packet Monitor, open Command Prompt as **Administrator**:

```powershell
pktmon start --capture --pkt-size 0
ping 8.8.8.8
pktmon stop
pktmon etl2pcap PktMon.etl -o packetcapture.pcapng
```

Open the generated `.pcapng` file in Wireshark. `tcpdump` and `ifconfig` are Unix/Linux tools; on Windows use Wireshark/Pktmon and `ipconfig` respectively.

### Experiments 02, 03, 07, 11, 13 and 14 — Single Python programs

Run the corresponding `.py` file with:

```powershell
py "EXACT FILE NAME.py"
```

For Experiment 03, the program makes a plain HTTP request on TCP port 80. Some websites redirect to HTTPS or block plain HTTP; test with a host that accepts HTTP. The public-IP lookup in Experiment 02 requires internet access.

### Experiments 04, 05 and 06 — TCP client/server programs

Each file offers a small menu. Use **two separate Command Prompt windows** on the same computer.

1. In Window 1, change to the repository folder and run the Python file.
2. Select the **server** option.
3. In Window 2, change to the same repository folder, run the same file, and select the **client** option.
4. Exchange messages or transfer a file.
5. Stop the server using `Ctrl+C` after the client exits.

Example for Experiment 04:

```powershell
py "Experiment 04 - TCP Echo Client and Server.py"
```

Run it once as server and again in the second window as client. Follow the same process for Experiments 05 and 06. For file transfer, place the source file in the client's current working directory or enter its full path. The server saves the received copy with the prefix `received_`.

These demonstrations bind to `127.0.0.1` and are intended for testing on one computer. Windows Firewall may prompt for permission; allow only the private/local network context needed for your test.

### Experiments 08–10 and 12 — NS-2 simulations

**Important:** NS-2 and NAM are primarily used in Linux lab environments. A standard Windows installation does not provide the `ns` and `nam` commands. On Windows, use a supported Linux environment such as an Ubuntu virtual machine or WSL 2 with a compatible NS-2/NAM installation. NAM requires a graphical environment; GUI support must be configured in that Linux environment.

After NS-2 and NAM are installed and available in the Linux terminal, change to the repository directory and run:

```bash
ns "Experiment 08 - TCP and UDP Simulation using NS2.tcl"
ns "Experiment 09 - Distance Vector Routing using NS2.tcl"
ns "Experiment 10 - Link State Routing using NS2.tcl"
ns "Experiment 12 - Link State Routing using NS2.tcl"
```

The scripts create trace files and NAM animation files in the current working directory. If NAM does not launch automatically, open the generated `.nam` file with:

```bash
nam link_state.nam
```

Use the output filename printed or defined in the script. These NS-2 experiments are not native PowerShell commands.

### Experiments 15–17 — Wireshark on Windows

1. Install Wireshark and Npcap from [wireshark.org](https://www.wireshark.org/download.html).
2. Launch Wireshark with the required capture permissions.
3. Select the active Wi-Fi or Ethernet interface and start capture.
4. Generate test traffic with `ping` or `nslookup`.
5. Enter the display filter in Wireshark's filter bar, for example:

```text
dns
icmp
tcp.flags.syn == 1 && tcp.flags.ack == 0
rtp
rtcp
```

Experiment 15 also documents capture filters. Enter those before starting the capture through **Capture → Options**. Capture filters use BPF syntax; display filters use Wireshark syntax. Do not interchange them.

For Experiment 16, an RTP/VoIP call or a supplied RTP capture is needed. Open **Telephony → RTP → RTP Streams**, select a stream, and click **Analyze** to inspect loss, jitter, delta, and sequence information.

For Experiment 17, inspect packet layers, use **Follow → TCP Stream**, and explore **Statistics → Protocol Hierarchy**, **Conversations**, and **Endpoints**.

### Experiment 18 — Cisco Packet Tracer on Windows

1. Install Cisco Packet Tracer (8.x recommended).
2. Add one 2960 switch and three PCs.
3. Connect each PC's FastEthernet0 interface to a switch port using Copper Straight-Through cables.
4. Configure these static addresses under each PC's **Desktop → IP Configuration**:

| Device | IPv4 address | Subnet mask |
|---|---|---|
| PC0 | `192.168.1.1` | `255.255.255.0` |
| PC1 | `192.168.1.2` | `255.255.255.0` |
| PC2 | `192.168.1.3` | `255.255.255.0` |

5. From a PC's **Desktop → Command Prompt**, test:

```text
ping 192.168.1.2
ping 192.168.1.3
```

6. Save the topology as a `.pkt` file.

### Experiment 19 — Benchmark LAN Trainer Kit

This is a **physical lab experiment**, not a Windows executable. Use the Benchmark LAN Trainer Kit, node modules, central hub/switch module, patch cords, power supply, and indicator panel.

Construct bus, star, ring, and mesh arrangements following the experiment file. Observe data paths and the effect of link failures. Study tree and hybrid topology concepts as described in the manual. Record the actual cable count and observations from the available kit.

## Topics covered

- **Network commands:** IP configuration, ping, active connections, DNS lookup, route tracing, and packet capture.
- **Python networking:** hostname/IP lookup, HTTP over TCP, echo service, chat, file transfer, and local DNS interface discovery.
- **Address resolution and error detection:** ARP, RARP, and CRC.
- **Network simulation:** TCP/UDP traffic and Distance Vector / Link State routing using NS-2.
- **Packet analysis:** Wireshark capture/display filters, RTP stream quality, and protocol inspection.
- **Network design:** Cisco Packet Tracer LAN and physical LAN topologies.

## Safety and reproducibility

- Capture packets only on networks and devices where you have permission.
- Run port checks only against systems you own or are explicitly authorized to test.
- The Python socket programs use localhost for client/server demonstrations.
- Do not expose unauthenticated demonstration servers to public networks.
- RTP measurements and Wireshark packet observations depend on the traffic captured; do not copy sample figures as actual results.
- NS-2 and NAM command availability depends on the configured Linux environment.
- Experiment 19 requires the physical trainer kit and cannot be reproduced by running a Windows command.

## Academic context

Computer Networks Laboratory — **Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya (SCSVMV University)**, B.Tech. Computer Science and Engineering.

## Related coursework repositories

- [DBMS Laboratory](https://github.com/surya-scsvmv/DBMS)
- [Java Programming Lab](https://github.com/surya-scsvmv/JAVA)
- [C++ Programming Lab](https://github.com/surya-scsvmv/CPP)
- [Data Structures and Algorithms](https://github.com/surya-scsvmv/DSA)
- [Design and Analysis of Algorithms](https://github.com/surya-scsvmv/DAA)
- [Data Visualization Lab](https://github.com/surya-scsvmv/DV)

---

<p align="center">Learn the protocol. Run the experiment. Observe the network.</p>
