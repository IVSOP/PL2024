#!/usr/bin/env python3

import sys
import re

flag = False
total = 0

for line in sys.stdin:
	matches = re.findall(r'(on|off|=|\d+)', line, re.I) # match de qualquer caso relevante

	for match in matches:
		
		if re.match(r'on', match, re.I):
			flag = True
		elif re.match(r'off', match, re.I):
			flag = False
		elif re.match(r'[0-9]+', match):
			if flag:
				total += int(match)
		elif re.match(r'=', match):
			print(f"Soma = {total}")

	print(matches)
