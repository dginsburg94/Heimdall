#!/usr/bin/env python3
from VirusTotalRequest import virusTotal
from SnortRuleGenerator import generator
import os

whitelist_dict = None

def checkwhitelistDict():
    global whitelist_dict
    if whitelist_dict:
        return True
    else:
        if os.path.exists('whitelist.txt'):
            with open('whitelist.txt', 'r') as inf:
                whitelist_dict = eval(inf.read())
        else:
            inf = open('whitelist.txt', 'w+')
            inf.write(r'{}')
            whitelist_dict = eval(inf.read())
            inf.close()
        return True

def towhiteList(hostname, status):
    #open whitelist file as a dictionary

#    with open('whitelist.txt', 'r') as inf:
#        whitelist_dict= eval(inf.read())
    #create new key value pair
    dict = {hostname:status}

    # add key value to dictionary
    whitelist_dict.update(dict)

#    inf.close()
    #open fiile and write the new dictionary to file
    with open('whitelist.txt', 'w') as winf:
        winf.write(str(whitelist_dict))
        winf.close()

    return

def checkwhitelist(hostname):
    global whitelist_dict
    exists_or_not = checkwhitelistDict()
    if exists_or_not:
        if hostname in whitelist_dict.keys():
            return
        elif hostname not in whitelist_dict.keys():
            virusTotalresp = virusTotal(hostname)
            if virusTotalresp:
                generator(hostname)
                status = 'malicious'
            elif virusTotalresp == None:
                return
            else:
                status = 'safe'
            towhiteList(hostname, status)