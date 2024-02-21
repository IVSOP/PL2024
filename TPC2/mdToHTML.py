#!/usr/bin/env python3

import sys
import re

paragraph_r = r"^# .+$"

bold_r      = r"(\*\*.*?\*\*)" # sem os parenteses as matches nao sao mostradas # !!!!! ? significa match as few times as possible
italic_r    = r"(\*.*?\*)"

image_r     = r"(\!\[.*\]\(.*\))"
link_r      = r"(\[.*\]\(.*\))"

list_r      = r"(^\<p\>[0-9]+\. .*$)"

lines = sys.stdin.readlines()

# muito mal feito
def parseBolds(strings):
	res = ""
	for string in strings:
		if re.match(bold_r, string):
			res += "<b>" + string[2:-2] + "</b>"
		else:
			res += string
	return res

# muito mal feito
def parseItalic(strings):
	res = ""
	for string in strings:
		if re.match(italic_r, string):
			res += "<i>" + string[1:-1] + "</i>"
		else:
			res += string
	return res

# muito mal feito
def parseImages(strings):
	res = ""
	for string in strings:
		if re.match(image_r, string):
			alt, link = re.split(r"\]\(", string)
			res += f"""<img src="{link[:-1]}" alt="{alt[2:]}" """
		else:
			res += string
	return res

def parseLinks(strings):
	res = ""
	for string in strings:
		if re.match(link_r, string):
			text, link = re.split(r"\]\(", string)
			res += f"""<a href="{link[:-1]}">{text[1:]}</a>"""
		else:
			res += string
	return res

def removeNumbers(string):
	return re.sub(r"[0-9]+\. ", '', string)

def parseListasAux(curLine, lineIter):
	res = f"""<ol>
<li>{removeNumbers(curLine[:-1])}</li>\n"""

	while True:
		try:
			line = next(lineIter)

			if re.match(list_r, line):
				res += f"<li>{removeNumbers(line[:-1])}</li>\n"
			else:
				break
		except StopIteration:
			break


	return res + "</ol>"

def parseListas(lines):
	lineIter = iter(lines)
	res = ""
	while True:
		try:
			line = next(lineIter)
			
			if re.match(list_r, line):
				res += parseListasAux(line, lineIter)
			else:
				res += line
		except StopIteration:
			break
	return res



def parseLines(lines):
	parsedLines = []

	for line in lines:

		if re.match(paragraph_r, line):
			line = "<h1>" + line[2:-1] + "</h1>\n" #-1 porque ultimo vai ser \n
		else:
			line = "<p>" + line[:-1] + "</p>\n"

		line = parseBolds(re.split(bold_r, line))
		# print("-------------------- after bold")
		# print(new)
		line = parseItalic(re.split(italic_r, line))
		# print("-------------------- after italic")
		# print(new)
		line = parseImages(re.split(image_r, line))
		# print("-------------------- after image")
		# print(new)
		line = parseLinks(re.split(link_r, line))

		parsedLines.append(line)

	# listas sao meio edge case porque envolvem varias linhas
	return parseListas(parsedLines)

print(parseLines(lines))
