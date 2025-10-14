# Activity 16: Point-to-Point Network Simulation (NS-3)

## Objective
To simulate a **simple point-to-point network** using NS-3 and analyze basic network communication between two nodes.

## Background

A **point-to-point network** is the simplest type of network — it connects two nodes directly using a dedicated link.  
In this activity, you will:
- Create two nodes (`n0`, `n1`)
- Connect them with a point-to-point channel
- Install Internet protocol stacks
- Set up UDP Echo Client and Server applications
- Observe packet transmission and latency

## Prerequisites
Before starting:
1. NS-3 must be installed on your RPi or Linux machine.  
2. Verify your setup:
   ```bash
   ./ns3 run hello-simulator
   ```
   If it prints `Hello Simulator`, you’re ready to go!

## 🧠 Network Topology

```
+--------+      5 Mbps, 2 ms      +--------+
|  Node0 |------------------------|  Node1 |
|  (Client)                       | (Server)|
+--------+                        +--------+
```

## Step 1: Create and Build the Script

### **Python Version**

Save as `point_to_point.py` inside your NS-3 `scratch/` folder.

```python
import ns.applications
import ns.core
import ns.internet
import ns.network
import ns.point_to_point

# Create two nodes
nodes = ns.network.NodeContainer()
nodes.Create(2)

# Create and configure point-to-point channel
p2p = ns.point_to_point.PointToPointHelper()
p2p.SetDeviceAttribute("DataRate", ns.core.StringValue("5Mbps"))
p2p.SetChannelAttribute("Delay", ns.core.StringValue("2ms"))

# Install network devices on nodes
devices = p2p.Install(nodes)

# Install Internet stack
stack = ns.internet.InternetStackHelper()
stack.Install(nodes)

# Assign IP addresses
address = ns.internet.Ipv4AddressHelper()
address.SetBase(ns.network.Ipv4Address("10.1.1.0"),
                ns.network.Ipv4Mask("255.255.255.0"))
interfaces = address.Assign(devices)

# Create UDP Echo Server on Node 1
echoServer = ns.applications.UdpEchoServerHelper(9)
serverApps = echoServer.Install(nodes.Get(1))
serverApps.Start(ns.core.Seconds(1.0))
serverApps.Stop(ns.core.Seconds(10.0))

# Create UDP Echo Client on Node 0
echoClient = ns.applications.UdpEchoClientHelper(
    interfaces.GetAddress(1), 9)
echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(5))
echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(1.0)))
echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(1024))

clientApps = echoClient.Install(nodes.Get(0))
clientApps.Start(ns.core.Seconds(2.0))
clientApps.Stop(ns.core.Seconds(10.0))

# Enable packet capture
p2p.EnablePcapAll("point_to_point")

# Run simulation
ns.core.Simulator.Run()
ns.core.Simulator.Destroy()
```

Run the simulation:
```bash
./ns3 run scratch/point_to_point.py
```

## Step 2: Analyze Results

### 1. View Console Output
You should see something like:
```
Sent 1024 bytes from 10.1.1.1 to 10.1.1.2
Received 1024 bytes from 10.1.1.2
```

### 2. View Packet Capture
Open the generated `.pcap` file in **Wireshark**:
```bash
wireshark point_to_point-0-0.pcap &
```
You can inspect packet headers, delays, and sequence numbers.

## Step 3: Experiment

Try modifying:
- Data rate (`1Mbps`, `10Mbps`)
- Delay (`5ms`, `10ms`)
- Packet size (`512`, `2048`)
- Number of packets

Observe how these changes affect the total delay and throughput.

## Discussion Questions

1. What happens if you increase the link delay from `2ms` to `10ms`?  
2. How does increasing `PacketSize` affect transmission time?  
3. Why is the server started before the client in the simulation?

## Expected Outcome
- Successful echo reply packets between Node0 and Node1  
- Generation of `.pcap` trace files  
- Understanding of basic point-to-point communication and latency factors
