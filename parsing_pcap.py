
import dpkt

f = open('pkts.pcap')
pcap = dpkt.pcap.Reader(f)

#for ts, buf in pcap:
def parsing(ts, buf):
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    #print ip
    tcp = ip.data

    #print tcp
    if tcp.dport == 80 and len(tcp.data) > 0:
        http = dpkt.http.Request(tcp.data)
        print http.uri

pcap.loop(parsing)

f.close()