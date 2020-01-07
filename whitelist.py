#!/usr/bin/env python3


def towhiteList(url, status):
    #open whitelist file as a dictionary
    with open('whitelist.txt', 'r') as inf:
        whitelist_dict= eval(inf.read())
    #create new key value pair
    dict = {url:status}

    # add key value to dictionary
    whitelist_dict.update(dict)

    inf.close()
    #open fiile and write the new dictionary to file
    with open('whitelist.txt', 'w') as winf:
        winf.write(str(whitelist_dict))
        winf.close()

    return

def checkwhitelist(url):
    # open the file as inf and eval it to be a dictionary whitelist_dict
    with open('whitelist.txt', 'r') as inf:
        whitelist_dict= eval(inf.read())

        #print the dictionary
        print(whitelist_dict)

    #if the url is in the dictionary close the file and return (exit function) to parser loop
    if url in inf.keys():
        inf.close()
        return

    #if url not in the dictionary it is going to run the virustotal function on the url and add to whitelist funciton
    elif url not in inf.keys():
        virustotal(url)
        towhiteList(url)
        inf.close()



towhiteList('poolstaff.com','safe')
#checkwhitelist()
