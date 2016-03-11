import random


import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import re

def fetch_data(url, params):
  
    if 'os' in params:
        if params['os'] == "ios":
           os_v = 0
        elif params['os'] == "android":
           os_v = 1
        else:
           os_v = "none"		  
    else:
       os_v = "none"

    if 'net' in params:
        if params['net'] == "3G":
           net_v = 0
        else:
           net_v = 1	
    else:
       net_v = "none"
	   
    if "isp" in params:
        isp_v = params['isp'].encode("gbk")
    else:
        isp_v = ""
	

#http://logpage.p2p.baofeng.com:8000//projects/wireless/critical/critical.php?begintime=2016-01-02&endtime=2016-03-08&
#nettype=none&servicetype=none&timedimention=d&random=0.54&os=0
    values = {'begintime' : "2016-01-02",
              'endtime' : "2016-05-08",
              'bitstream' : "none",
              'nettype' : net_v,
			  'servicetype' :"none",
              'timedimention' : "d",
              'os' : os_v,
			  'txtTypesIsp' : isp_v,
              'random' : random.random(),

	}

    ''' exclude isp & os , all must transform
    for k, v in params.items():
        values[k] = v
    '''
	
			  
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
    url = 'http://logpage.p2p.baofeng.com:8000/projects/wireless/critical/critical.php'

    return get_data_filter(fields, url, params)


def get_playfeel(fields, params):
	if params['os'] == "ios":
		url = 'http://logpage.p2p.baofeng.com:8000/projects/wireless/wliosplayfeel/playfeel.php'
	else:
		url = 'http://logpage.p2p.baofeng.com:8000/projects/wireless/wladroplayfeel/playfeel.php'

	return get_data_filter(fields, url, params)

def get_mplay(fields, params):
	if params['os'] == "ios":
		url = 'http://logpage.p2p.baofeng.com:8000/projects/wireless/wliosmplay/mplay.php'
	else:
		url = 'http://logpage.p2p.baofeng.com:8000/projects/wireless/wladromplay/mplay.php'
		
   
	return get_data_filter(fields, url, params)

def get_punch(fields, params):
    url = 'http://logpage.p2p.baofeng.com:8000/projects/wireless/punch/punch.php'

    return get_data_filter(fields, url, params)


  