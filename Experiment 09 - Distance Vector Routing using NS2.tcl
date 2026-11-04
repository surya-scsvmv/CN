# AIM:
# To simulate Distance Vector Routing Algorithm using the NS-2 simulation tool.
#
# ALGORITHM:
# 1. Create an NS-2 simulator and select Distance Vector routing using rtproto DV.
# 2. Open NAM and trace files.
# 3. Create eight nodes and connect them in a ring topology using duplex links.
# 4. Attach a UDP source and Null destination, and connect them.
# 5. Attach a CBR traffic generator and configure packet size and interval.
# 6. Schedule traffic, a link failure, link recovery, and simulation termination.
# 7. Run NS-2 and observe the routing response in NAM.

set ns [new Simulator]
$ns rtproto DV

set nf [open out.nam w]
$ns namtrace-all $nf
set nt [open trace.tr w]
$ns trace-all $nt

proc finish {} {
    global ns nf nt
    $ns flush-trace
    close $nf
    close $nt
    exec nam -a out.nam &
    exit 0
}

set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]
set n8 [$ns node]

$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n4 $n5 1Mb 10ms DropTail
$ns duplex-link $n5 $n6 1Mb 10ms DropTail
$ns duplex-link $n6 $n7 1Mb 10ms DropTail
$ns duplex-link $n7 $n8 1Mb 10ms DropTail
$ns duplex-link $n8 $n1 1Mb 10ms DropTail

$ns duplex-link-op $n1 $n2 orient left-up
$ns duplex-link-op $n2 $n3 orient up
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n4 $n5 orient right
$ns duplex-link-op $n5 $n6 orient right-down
$ns duplex-link-op $n6 $n7 orient down
$ns duplex-link-op $n7 $n8 orient left-down
$ns duplex-link-op $n8 $n1 orient left

set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0

set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

set null0 [new Agent/Null]
$ns attach-agent $n4 $null0
$ns connect $udp0 $null0

$ns at 0.0 "$n1 label Source"
$ns at 0.0 "$n4 label Destination"
$ns at 0.5 "$cbr0 start"
$ns rtmodel-at 1.0 down $n3 $n4
$ns rtmodel-at 2.0 up $n3 $n4
$ns at 4.5 "$cbr0 stop"
$ns at 5.0 "finish"
$ns run
