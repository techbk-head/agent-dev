import pcap
def print_pkt(ts, pkt, arg):
	print repr(pkt)

pc = pcap.pcap()
pc.loop(-1,print_pkt)