#!/usr/bin/env python 

#import json
from logging import root
import requests
#from bs4 import BeautifulSoup
import re

_config_filename = 'settings.json'

_website = "https://example.com"
_sitemap_uri = "/sitemap.xml"
_search_string = "lorem" 


if __name__ == '__main__':

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
            if sitemap.getchildren():
                children = sitemap.getchildren()
                urlList.append(children[0].text)
        print(urlList)
            #for x in elt:
            #    print(x.tag, x.attrib, x.getchildren())
            #    print(dir(x))

        loremList = []
        # scrape eache URI
        for url in urlList:
            r = session.get(url)
            if re.search(_search_string, r.text, re.IGNORECASE):
                loremList.append(url)

        print(loremList)
