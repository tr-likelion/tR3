#-*- coding: utf-8 -*-
# JTBC 뉴스 속보 xml문서 파싱하기
# import webbrower

import urllib
from xml.etree.ElementTree import parse

from bs4 import BeautifulSoup
import urllib2

xml = urllib.urlopen('http://www.khan.co.kr/rss/rssdata/kh_world.xml')	# global

tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
root = tree.getroot()	# root태그 얻어오기



i = 0
for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):	# item 태그를 모두 반복
		i += 1
		print i,
		# for i in range(1,len("title")):	 
		print child.find("title").text


print 
num = raw_input ("보고 싶은 뉴스 번호를 입력하세요 :")
num = int(num)

for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):	# item 태그를 모두 반복
		i += 1
		print i,
		# for i in range(1,len("title")):	 
		print child.find("title")

		url = child.find("link")
		print url

		webbrower.open(url)
		print 
		
#		뉴스 제목 보기
#		print child.findtext("title")
		
		# 뉴스 내용 보기
#		print child.findtext("description")
