#!/usr/bin/env python3

#takes generated rule and adds it to a snort rules file
def addrule(snortrule):
    f = open('/etc/snort/rules/Snort_Generator_Rules.rules','w+')
    f.write(snortrule)
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
    message = f"msg: 'user/program accessing' {url}"
    content = f"content: \"{url}\" "
    flowout = '->'
    flowin = '<-'

#putting together the rule
    rule = f'#{alert} {protocal} {sourceip} any {flowout} {destinationip} any ({content}; {message};)'
    addrule(rule)
