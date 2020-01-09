#!/usr/bin/env python3
import pcap
import dpkt
from dpkt.tcp import TCP
from whitelist import checkwhitelist

def CapParse():
    interface = input('Please enter the interface for packet capture: ')
    pc = pcap.pcap(interface)

    for ts, buf in pc:
        eth = dpkt.ethernet.Ethernet(buf)
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue
        ip = eth.data
        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue
        tcp = ip.data
        data= tcp.data
        if not isinstance(tcp, TCP):
            continue
        # if it is tcp packet with a destination of port 80 get uriz
        try:
            if tcp.dport == 80 and len(tcp.data) > 0:
                http = dpkt.http.Request(tcp.data)
                url = http.headers['host']+http.uri
                
                hostname = http.headers['host']
            
            checkwhitelist(hostname)
        except:
            continue