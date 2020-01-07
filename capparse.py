#!/usr/bin/env python3

import dpkt
from dpkt.tcp import TCP

def CapParse():
    #open pcap file
    f = open('network.pcap', 'rb')

    #crerate pcap object
    pcap = dpkt.pcap.Reader(f)

    #enumerate packets by timestamp
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data

        #if not a tcp packet
        if not isinstance(tcp, TCP):
            continue
        # if it is tcp packet with a destination of port 80 get uri
        if tcp.dport == 80 and len(tcp.data) > 0:
            http = dpkt.http.Request(tcp.data)
            url= http.headers['host']+http.uri
            # if the http is within our whitelist continue onto the next tcp packet
        #    if http in wlist:
        #        continue
            # if it is not in the whitelist then submit to virus total for checking
    #        else:
            #    virustotal(url)
            print(url)


    f.close()

CapParse()
