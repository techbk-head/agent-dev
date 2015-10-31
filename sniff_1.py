import pcap
def print_pkt(ts, pkt):
	print repr(pkt)
	print "----------------------------------------------------------------"
pc = pcap.pcap('wlan0')
pc.loop(print_pkt)
