import pcap
pc = pcap.pcap()


def __my_handler(ts,pkt,d):
	print pkt

pc.loop(0,__my_handler)
