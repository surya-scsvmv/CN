# Computer Networks Laboratory

A structured collection of **Computer Networks (CN) laboratory experiments** covering network configuration, connectivity testing, packet inspection, DNS, TCP/UDP socket programming, ARP/RARP, and routing simulations using **NS-2**.

<p>
  <img src="https://img.shields.io/badge/Focus-Computer%20Networks-2563EB?style=flat-square" alt="Computer Networks"/>
  <img src="https://img.shields.io/badge/Python-Socket%20Programming-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python socket programming"/>
  <img src="https://img.shields.io/badge/Simulator-NS--2-0F766E?style=flat-square" alt="NS-2"/>
  <img src="https://img.shields.io/badge/Experiments-11-7C3AED?style=flat-square" alt="11 experiments"/>
</p>

## Experiment index

| No. | Experiment | File |
|---:|---|---|
| **01** | Network commands, configuration, connectivity, route tracing, and packet analysis | [Experiment 01](<Experiment 01 - Network Commands and Packet Analysis.txt>) |
| **02** | Machine hostname, local/public IP, DNS lookup, ping, and service-port checks using Python | [Experiment 02](<Experiment 02 - Machine Hostname and IP Address.py>) |
| **03** | HTTP GET request using a TCP socket | [Experiment 03](<Experiment 03 - HTTP Web Client and Server using TCP Sockets.py>) |
| **04** | TCP echo client and server | [Experiment 04](<Experiment 04 - TCP Echo Client and Server.py>) |
| **05** | Multi-client TCP chat application using threads | [Experiment 05](<Experiment 05 - TCP Multi-Client Chat Application.py>) |
| **06** | TCP client-server file transfer | [Experiment 06](<Experiment 06 - TCP File Transfer.py>) |
| **07** | ARP and RARP lookup simulation | [Experiment 07](<Experiment 07 - ARP and RARP Protocol.py>) |
| **08** | TCP and UDP traffic simulation using NS-2 | [Experiment 08](<Experiment 08 - TCP and UDP Simulation using NS2.tcl>) |
| **09** | Distance Vector routing simulation using NS-2 | [Experiment 09](<Experiment 09 - Distance Vector Routing using NS2.tcl>) |
| **10** | Link State routing simulation using NS-2 | [Experiment 10](<Experiment 10 - Link State Routing using NS2.tcl>) |
| **11** | Local hostname and IP address discovery using Python sockets | [Experiment 11](<Experiment 11 - Local DNS and IP Address.py>) |

## Topics covered

- **Network fundamentals:** IP configuration, subnet and gateway information, MAC addresses, connectivity checks, active connections, DNS resolution, and route tracing.
- **Packet analysis:** packet capture concepts and tools such as Wireshark and Windows Packet Monitor (Pktmon).
- **Python networking:** hostname and IP discovery, DNS lookups, TCP client-server communication, HTTP requests, multithreaded chat, and file transfer.
- **Address resolution:** ARP and RARP mapping concepts.
- **Network simulation:** TCP/UDP traffic, Distance Vector routing, and Link State routing with NS-2.

## Requirements

Install the tools relevant to the experiment you want to run. You do not need every tool for every experiment.

| Tool | Used for |
|---|---|
| **Python 3** | Experiments 02–07 and 11 |
| **NS-2** | Experiments 08–10 |
| **NAM (Network Animator)** | Visualizing NS-2 simulation output |
| **Wireshark / Pktmon** | Packet capture and inspection in Experiment 01 |
| **Windows Command Prompt / PowerShell** | Windows network commands in Experiment 01 |
| **Linux terminal** | Linux equivalents of common network commands |

### Python setup

Check that Python is installed:

```bash
python --version
```

The Python networking examples primarily use the standard library, including `socket`, `threading`, `os`, and `urllib`. No third-party package is required for the basic examples.

### NS-2 setup

Install a compatible NS-2 environment and NAM. Verify that the `ns` and `nam` commands are available:

```bash
ns
nam
```

NS-2 installation steps vary by operating system and distribution. Use an environment supported by your lab setup.

## Running the experiments

Clone the repository:

```bash
git clone https://github.com/surya-scsvmv/CN.git
cd CN
```

### Python experiments

Run the relevant Python file from the repository directory:

```bash
python "Experiment 02 - Machine Hostname and IP Address.py"
python "Experiment 03 - HTTP Web Client and Server using TCP Sockets.py"
python "Experiment 07 - ARP and RARP Protocol.py"
python "Experiment 11 - Local DNS and IP Address.py"
```

For client-server experiments (**04–06**), start the server role first and then connect from the client role. The files contain the corresponding client/server code; check the entry-point sections and run the two roles separately where necessary. Use the same host and port settings on both ends.

### NS-2 simulations

Run an NS-2 script from the repository directory:

```bash
ns "Experiment 08 - TCP and UDP Simulation using NS2.tcl"
ns "Experiment 09 - Distance Vector Routing using NS2.tcl"
ns "Experiment 10 - Link State Routing using NS2.tcl"
```

The scripts generate trace or NAM output files in the working directory. Open a generated NAM file with NAM when the simulation script has not already launched it:

```bash
nam out.nam
```

Experiment 10 writes `link_state.nam` and `link_state.tr`; its NAM output can be opened with:

```bash
nam link_state.nam
```

Output filenames and visualization behavior depend on the individual script.

## Suggested lab workflow

1. Read the experiment file and identify its objective.
2. Check the required operating system, runtime, simulator, and permissions.
3. Inspect the commands or source code before execution.
4. Run the experiment with a small, controlled test case.
5. Record the observed output, packet behavior, or routing result in your lab record.
6. Note any environment-specific changes needed to reproduce the result.

## Safety and usage notes

- Run packet captures only on devices and networks where you have permission.
- Use port checks and connectivity tests only against systems you own or are explicitly authorized to assess.
- The public-IP lookup in Experiment 02 uses an external IP lookup service and therefore requires internet access.
- TCP client-server examples are intended for controlled local testing. Do not expose unauthenticated demonstration servers to untrusted networks.
- Review file paths and transfer behavior before sending or receiving files.
- NS-2 trace and NAM files are generated artifacts; they may be recreated when the simulations are run.

## Academic context

Computer Networks Laboratory coursework — **Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya (SCSVMV University)**, B.Tech. Computer Science and Engineering (AI & Data Science).

## Related coursework repositories

- [DBMS Laboratory](https://github.com/surya-scsvmv/DBMS)
- [Java Programming Lab](https://github.com/surya-scsvmv/JAVA)
- [C++ Programming Lab](https://github.com/surya-scsvmv/CPP)
- [Data Structures and Algorithms](https://github.com/surya-scsvmv/DSA)
- [Design and Analysis of Algorithms](https://github.com/surya-scsvmv/DAA)
- [Data Visualization Lab](https://github.com/surya-scsvmv/DV)


---

<p align="center">Learn the protocol. Run the experiment. Observe the network.</p>
