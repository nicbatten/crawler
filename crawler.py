#!/usr/bin/env python

import requests



def request(url):
    try:
        return requests.get("http://" + url)
        #get_response = requests.get("http://" +  url)
        #print(get_response)
    except requests.exceptions.ConnectionError:
        pass

target_url="google.com"

with open("/root/PycharmProjects/crawler/wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        #print(test_url)
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)
