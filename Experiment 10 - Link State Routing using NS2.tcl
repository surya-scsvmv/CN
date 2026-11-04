# AIM: To simulate Link State routing using NS-2.
# ALGORITHM:
# 1. Create an NS-2 simulator, trace file, and NAM file.
# 2. Enable the Link State routing protocol and create six network nodes.
# 3. Connect the nodes with multiple possible routes.
# 4. Generate UDP/CBR traffic from source node 0 to destination node 5.
# 5. Schedule a link failure and restoration, then observe route recomputation.
# 6. Run the simulation and inspect the trace and NAM animation.

set ns [new Simulator]
set tracefile [open "link_state.tr" w]
set namfile [open "link_state.nam" w]
$ns trace-all $tracefile
$ns namtrace-all $namfile
$ns rtproto LS
for {set i 0} {$i < 6} {incr i} {
    set n($i) [$ns node]
}
$ns duplex-link $n(0) $n(1) 2Mb 10ms DropTail
$ns duplex-link $n(1) $n(2) 2Mb 10ms DropTail
$ns duplex-link $n(2) $n(5) 2Mb 10ms DropTail
$ns duplex-link $n(0) $n(3) 2Mb 10ms DropTail
$ns duplex-link $n(3) $n(4) 2Mb 10ms DropTail
$ns duplex-link $n(4) $n(5) 2Mb 10ms DropTail
$ns duplex-link $n(1) $n(4) 1Mb 15ms DropTail
$ns duplex-link-op $n(0) $n(1) orient right-down
$ns duplex-link-op $n(1) $n(2) orient right-down
$ns duplex-link-op $n(2) $n(5) orient down
$ns duplex-link-op $n(0) $n(3) orient right-up
$ns duplex-link-op $n(3) $n(4) orient right-up
$ns duplex-link-op $n(4) $n(5) orient right-up
set udp [new Agent/UDP]
$ns attach-agent $n(0) $udp
set sink [new Agent/Null]
$ns attach-agent $n(5) $sink
$ns connect $udp $sink
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 512
$cbr set interval_ 0.05
$cbr attach-agent $udp
$ns at 0.5 "$cbr start"
$ns at 2.0 "$ns link $n(1) $n(2) down"
$ns at 3.5 "$ns link $n(1) $n(2) up"
$ns at 4.5 "$cbr stop"
proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    puts "Link State Routing simulation completed."
    puts "Trace: link_state.tr | NAM: link_state.nam"
    exec nam link_state.nam &
    exit 0
}
$ns at 5.0 "finish"
$ns run