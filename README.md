# Heimdall

Heimdall is a command line tool for analyzing HTTP traffic and using the VirusTotal api to identify malicious domains and write Snort Rules to block web traffic to them.

Before using Heimdall create a file in the same working directory called special.py with your api key set to the a variable called key.

To run Heimdall use the command sudo ./Heimdall.py

The first time Heimdall is ran it will create a file called whitelist.txt to be used for caching. It will also create a rule file in /etc/snort/rules named Snort_Rule_Generator.rules and append the main snort config file to include the new rule file.
Note: Future rules written to the rule file will initially be commented out and must be uncommented to be used by snort.

