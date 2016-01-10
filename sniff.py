import pcap
pc = pcap.pcap()


def __my_handler(ts,pkt):
	print pkt

pc.loop(__my_handler)
