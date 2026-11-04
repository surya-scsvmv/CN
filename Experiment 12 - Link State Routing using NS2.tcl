# AIM:
# To simulate the Link State Routing Algorithm using the NS-2 simulation tool.
#
# ALGORITHM:
# 1. Create an NS-2 simulator and open trace and NAM output files.
# 2. Create twelve nodes and connect them using the links described in the topology.
# 3. Attach two UDP agents and CBR traffic generators to source nodes.
# 4. Attach Null sink agents to the destination node and connect the traffic flows.
# 5. Enable the Link State routing protocol using rtproto LS.
# 6. Assign different flow identifiers and colors for the two traffic streams.
# 7. Schedule traffic, link failures, link recovery, and the simulation finish event.
# 8. Close the trace files and launch NAM to observe the simulation.

set ns [new Simulator]

set tracefile [open link_state.tr w]
set namfile [open link_state.nam w]
$ns trace-all $tracefile
$ns namtrace-all $namfile

for {set i 0} {$i < 12} {incr i} {
    set n($i) [$ns node]
}

for {set i 0} {$i < 8} {incr i} {
    $ns duplex-link $n($i) $n([expr $i + 1]) 1Mb 10ms DropTail
}

$ns duplex-link $n(0) $n(8) 1Mb 10ms DropTail
$ns duplex-link $n(1) $n(10) 1Mb 10ms DropTail
$ns duplex-link $n(0) $n(9) 1Mb 10ms DropTail
$ns duplex-link $n(9) $n(11) 1Mb 10ms DropTail
$ns duplex-link $n(10) $n(11) 1Mb 10ms DropTail
$ns duplex-link $n(11) $n(5) 1Mb 10ms DropTail

set udp0 [new Agent/UDP]
$ns attach-agent $n(0) $udp0

set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

set sink0 [new Agent/Null]
$ns attach-agent $n(5) $sink0
$ns connect $udp0 $sink0

set udp1 [new Agent/UDP]
$ns attach-agent $n(1) $udp1

set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 500
$cbr1 set interval_ 0.005
$cbr1 attach-agent $udp1

set sink1 [new Agent/Null]
$ns attach-agent $n(5) $sink1
$ns connect $udp1 $sink1

$ns rtproto LS
$ns rtmodel-at 10.0 down $n(11) $n(5)
$ns rtmodel-at 15.0 down $n(7) $n(6)
$ns rtmodel-at 20.0 up $n(7) $n(6)
$ns rtmodel-at 30.0 up $n(11) $n(5)

$udp0 set fid_ 1
$udp1 set fid_ 2
$ns color 1 Red
$ns color 2 Green

proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    exec nam link_state.nam &
    exit 0
}

$ns at 1.0 "$cbr0 start"
$ns at 2.0 "$cbr1 start"
$ns at 45.0 "finish"
$ns run
