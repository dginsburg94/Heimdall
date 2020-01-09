#!/bin/bash

current_dir=$(pwd)
ln -s $current_dir/SnortRuleGenerator.py /usr/local/bin
ln -s $current_dir/SnortRuleGenerator /etc/init.d/SnortRuleGenerator
ln -s $current_dir/SnortRuleGenerator /etc/rc5.d/S01SnortRuleGenerator
systemctl daemon-reload
systemctl enable SnortRuleGenerator.service
systemctl start SnortRuleGenerator
systemctl status SnortRuleGenerator
read -p 'Please enter the interface for packet capture: ' interface
echo '#!/usr/bin/env python3' > interface.py
echo 'interface = ' $interface >> interface.py
chmod +x *.py
chmod +x SnortRuleGenerator

