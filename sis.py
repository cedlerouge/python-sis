#!/usr/bin/env python 

"""
This scripts looks for a string in a website
and write in a csv file every URL that contains the string 
"""

#import json
from logging import root
import requests
from bs4 import BeautifulSoup
import re
import csv

_config_filename = 'settings.json'

_website = "https://example.com"
_sitemap_uri = "/sitemap.xml"
_search_string = "dupont"

if __name__ == '__main__':

    loremList = []

    # get xml content 
    with requests.Session() as session:
        r = session.get(_website + _sitemap_uri)
        print(r.text)

        #from lxml import etree
        #tree = etree.parse
        import xml.etree.ElementTree as ET
        root = ET.fromstring(r.text)
        #print(tree[0].tag)

        urlList = []
        for sitemap in root:
            #print(sitemap)
            if 'getchildren' in dir(sitemap):
                children = sitemap.getchildren()
                urlList.append(children[0].text)
            else:
                #print(sitemap.tag, sitemap.text)
                for x in sitemap:
                   print(x.tag,x.attrib,x.text)
                   if "loc" in x.tag:
                       urlList.append(x.text)

        # scrape eache URI
        for url in urlList:
            r = session.get(url)
            print(r.status_code, url)
            if re.search(_search_string, r.text, re.IGNORECASE):

                # Get the old url of the iframe to create the new url of the iframe
                soup = BeautifulSoup(r.text, 'html.parser')
                iframe = soup.find('iframe')
                new_url = iframe['src'].replace('dupont.nc', 'dupont.org')

                loremList.append({
                    "site_page": url,
                    "new_iframe_url": new_url
                    })

    with open("url.csv", 'w') as of:
        csv_writer = csv.writer(of, delimiter=';')
        # write result into csv file
        for url in loremList:
            csv_writer.writerow(url.values())
