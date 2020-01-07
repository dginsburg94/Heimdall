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
            url = http.headers['host']+http.uri

            # run checkwhitelist in order to check if the url has been checked before,
            # if it hasnt been checked it will run virustotal function
            #if it has it will go onto nextpacket

            checkwhitelist(url)
        #    print(http.headers['host']+http.uri)


    f.close()
