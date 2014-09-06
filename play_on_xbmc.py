#! /usr/bin/python

import requests
import json
import sys
import urlparse

xbmc_ip = "192.168.25.97"
xbmc_username = "xbmc"
xbmc_password = "xbmc"

def main(v_id):
	send_to_xbmc(v_id)
	j = get_title(v_id)
	print("Playing '{}'".format(j["data"]["title"]))

def parse_id(url):
	parsed_url = urlparse.urlparse(url)
	query = urlparse.parse_qs(parsed_url.query)
	return query["v"][0]

def send_to_xbmc(v_id):
	xbmc_url = "http://{}/jsonrpc?request=".format(xbmc_ip)
	payload = {"jsonrpc": "2.0", "method": "Player.Open", "params":{"item": {"file" : "plugin://plugin.video.youtube/?action=play_video&videoid={}".format(v_id) }}, "id" : "1"}
	requests.post(xbmc_url, auth=(xbmc_username, xbmc_password), data=json.dumps(payload))

def get_title(v_id):
	r = requests.get("http://gdata.youtube.com/feeds/api/videos/{}?v=2&alt=jsonc".format(v_id))
	return json.loads(r.content)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if "youtube" in sys.argv[1].lower():
			v_id = parse_id(sys.argv[1])
			main(v_id)
		else:
			main(sys.argv[1])
	else:
		respone = raw_input("What is the URL or ID of the YouTube video?\n> ")
		if "youtube" in respone.lower():
			v_id = parse_id(respone)
			main(v_id)
		else:
			main(v_id)