#!/bin/bash

ln -s ./SnortRuleGenerator.py /usr/local/bin
ln -s ./SnortRuleGenerator /etc/init.d/SnortRuleGenerator
ln -s ./SnortRuleGenerator /etc/rc5.d/S01SnortRuleGenerator
systemctl daemon-reload
systemctl enable SnortRuleGenerator.service
systemctl start SnortRuleGenerator
systemctl status SnortRuleGenerator
read -p 'Please enter the interface for packet capture: ' interface
echo '#!/usr/bin/env python3' > interface.py
echo 'interface = ${interface}' >> interface.py

