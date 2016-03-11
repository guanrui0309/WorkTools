import random


import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import re

def fetch_data(url, params):
  
   
    if "isp" in params:
        isp_v = params['isp'].encode("gbk")
    else:
        isp_v = ""
	

    values = {'begintime' : "2016-01-02",
              'endtime' : "2016-05-08",
              'bitstream' : "none",
			  'servicetype' :"none",
              'timedimention' : "d",
			  'orderby' : 'DaTotalDown',
			  'sortbycid' : 'false',
			  'txtTypesIsp' : isp_v,
              'random' : random.random(),

	}

			  
    encoded_params = urllib.parse.urlencode(values)
    full_url = url + "?" + encoded_params

    print(full_url)

    try:
        print("fetching data...")
        
        response = urllib.request.urlopen(full_url)
        content = response.read().decode('utf-8')

        print("got it")
		
        #print content
        return content

    except URLError as e:
        print(e.reason)


def get_data(sub_s, url, params):
    
    content = fetch_data(url, params)
    datas = []

    for v in sub_s:
        c = re.compile(v)
        items = c.findall(content)
        items.reverse()
        datas.append(items)

    return datas


def get_data_filter(fields, url, params):
    
    sub_s = [ re.compile('"' + v +'":"?([^,}"]*)', re.IGNORECASE) for v in fields]
    return get_data(sub_s, url, params)


def get_critical(fields, params):
    url = 'http://logpage.p2p.baofeng.com:8000/projects/vod/critical/critical.php'

    return get_data_filter(fields, url, params)

def get_punch(fields, params):
    url = 'http://logpage.p2p.baofeng.com:8000/projects/vod/punch/punch.php'

    return get_data_filter(fields, url, params)


  