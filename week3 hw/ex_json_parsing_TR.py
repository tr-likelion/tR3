#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")


data = json.load(htmltext)
 
print " MUM_NUM      Age         Job          MEM_CODE         etc"

for each in data['data']:
	print "%5s %10s %15s %15s" % (each['MEM_NUM'],each['age'], each['job'], each['MEM_CODE']),
	if each['age'] >= 50:
		print "%10s" % "Old"
	else:
		print "  "		

	

