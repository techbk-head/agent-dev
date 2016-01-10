import pcap, dpkt


def print_pkt(ts, pkt):
	pcw = dpkt.pcap.Writer(open('pkts.pcap','wb'))
	pcw.writepkt(ts, pkt)
#f = open("out.pcap", 'w')
#pc = pcap.pcap(dumpfile='out.pcap')
pc = pcap.pcap()
pc.loop(print_pkt)
