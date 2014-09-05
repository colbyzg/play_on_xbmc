#! /usr/bin/python

import requests
import json
import sys

xbmc_ip = "192.168.25.97"
xbmc_username = "xbmc"
xbmc_password = "xbmc"

def send_to_xbmc(v_id):
	xbmc_url = "http://{}/jsonrpc?request=".format(xbmc_ip)
	payload = {"jsonrpc": "2.0", "method": "Player.Open", "params":{"item": {"file" : "plugin://plugin.video.youtube/?action=play_video&videoid={}".format(v_id) }}, "id" : "1"}
	requests.post(xbmc_url, auth=(xbmc_username, xbmc_password), data=json.dumps(payload))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		send_to_xbmc(sys.argv[1])
	else:
		send_to_xbmc(raw_input("What is the ID of the YouTube video?\n> "))