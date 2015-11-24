"""
"""
import httplib
import xml.etree.ElementTree as ET
import socket

try:
	conn = httplib.HTTPConnection("api.bart.gov")
	conn.request("GET",
				 "/api/etd.aspx?cmd=etd&orig=ucty&key=MW9S-E7SL-26DU-VV8V")
	response = conn.getresponse()
	if response.status == 200:
		data = response.read()
		tree = ET.fromstring(data)

		station_list = []
		etd_list = []
		for child in tree.findall('station/etd'):
			for item in child.iter():
				if item.tag == "destination":
					station_list.append(item.text)
				if item.tag == "minutes":
					etd_list.append(item.text)
		print station_list, etd_list
			

except socket.error as error:
	print error




