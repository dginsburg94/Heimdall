#!/usr/bin/env python3

##takes generated rule and adds it to a snort rules file
def addrule(snortrule):
    f = open("rules.txt","w+")
    f.write(snortrule)
    f.close()


## takes malicious url and creates a snort rule around it
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
   rule = f"{alert} {protocal} {sourceip} any {flowout} {destinationip} any ({content}; {message};)"

#asking the user if they would like to add the created snort rule into the file
   print("this snort rule will be created: ")
   print(rule)
   accept = input("would you like to add to rules list? (Y/N)")

 #if they accept to add the rule addrule will be executed and rule will be added to the file
   if accept == 'Y':
       addrule(rule)
       return print('rule added')
   else:
       return print('rule was not added')

# generate rule
generator('cool.com')
