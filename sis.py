#!/usr/bin/env python 

#import json
import requests
#from bs4 import BeautifulSoup

_config_filename = 'settings.json'

_website = "https://betwit.lepont.bzh"
_sitemap_uri = "/sitemap.xml"
_search_string = "dupont" 


if __name__ == '__main__':

    # get xml content 
    with requests.Session() as session:
        r = session.get(_website + _sitemap_uri)
        print(r.text)

    # scrape earche URI 



    # list sucessful search pages
