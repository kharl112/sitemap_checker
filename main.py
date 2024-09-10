#!/usr/bin/python3
import urllib.request
from urllib.error import HTTPError, URLError

import xmltodict
import json

import sys



def get_url_contents(url):
  try:
    res = urllib.request.urlopen(url)
    content = res.read()

    return content


  except HTTPError as e:
    print(f"Eror url {url}: {e.code}: {e.reason}")
    return False
  except URLError as e:
    print(f"Eror url {url}: {e.reason}")
    return False
  except Exception as e:
    print(f"Eror url {url}: {e}")
    return False 


xml_data = get_url_contents('https://example.com/sitemap.xml')

if xml_data is not False:
  xml_dict = xmltodict.parse(xml_data)

  for row in xml_dict.get('urlset').get('url'):
    loc = row.get('loc')
    print(loc)

    res = get_url_contents(loc)
    if res is False:
      sys.exit(1)
else:
  sys.exit(1)






