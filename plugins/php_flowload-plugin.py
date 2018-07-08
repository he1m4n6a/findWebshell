#/usr/bin/env python
#coding=utf8

import re

rule='(include|require)(_once){0,1}[\s*]+[\"|\']+[0-9A-Za-z_]*\://'

def judgeBackdoor(fileCtent):
	result = re.compile(rule).findall(fileCtent)
	print result
	if len(result) > 0:
		return "流包装器加密后门"
	return None
