#!/usr/bin/env python3

#takes generated rule and adds it to a snort rules file
def addrule(snortrule):
    f = open('/etc/snort/rules/Snort_Generator_Rules.rules','a+')
    f.write('\r' + snortrule)
    f.close()
    fconf = open('/etc/snort/snort.conf','r')
    text = fconf.read()
    if 'include $RULE_PATH/Snort_Generator_Rules.rules' not in text:
        fconf.close()
        fconf = open('/etc/snort/snort.conf','a')
        fconf.write('include $RULE_PATH/Snort_Generator_Rules.rules')
        fconf.close()
        


# takes malicious url and creates a snort rule around it
def generator(url):
     
#variables defining the 5 tuple
    alert = 'alert'
    url = url
    protocal = 'tcp'
    sourceip = '$HOME_NET'
    destinationip = '$EXTERNAL_NET'
    message = f"msg: 'user/program accessing {url}'; react:block"
    content = f"content: \"{url}\" "
    flowout = '->'
    flowin = '<-'
    sid = 1000001
    try:
        f = open('/etc/snort/rules/Snort_Generator_Rules.rules','r')
        text = f.readlines()
        lastline = text[-1]
        lastline = lastline.rstrip()
        lastline = lastline.split()
        most_recent_sid = lastline[-1][4:-2]
        sid = int(most_recent_sid) + 1
    except:
        pass
#putting together the rule
    rule = f'#{alert} {protocal} {sourceip} any {flowout} {destinationip} any ({content}; {message}; sid:{sid};)'
    addrule(rule)
