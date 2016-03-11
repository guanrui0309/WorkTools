import matplotlib.pyplot as plt
from dateutil import parser

from get_wl_data import *

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

fig = plt.figure()

def view_downp2p(params, fmt, view, prefix):
	
    dates, P2PDownload, P2PRate = get_critical(['date', 'P2PDownload', 'P2PRate'], params)
    dates = [parser.parse(d) for d in dates]

    P2PDownload = [int(float(v))/(1024) for v in P2PDownload]

    plt.subplot(view)
    plt.ylabel(prefix + " P2P下载量(GB)")
    plt.plot_date(dates, P2PDownload, fmt, label=params['isp'])

    if view == 321 :
	    plt.legend(loc='upper left')

def view_punch(params, fmt, view, prefix):
    dates, PunchSuccRate = get_punch(['date', 'PunchSuccRate'], params)
    dates = [parser.parse(d) for d in dates]

    PunchSuccRate = [float(v)*100 for v in PunchSuccRate]

    plt.subplot(view)
    plt.ylabel(prefix + " 打孔成功率(%)")
    plt.plot_date(dates, PunchSuccRate, fmt, label=params['isp'])

    if view == 321 :
        plt.legend(loc='upper left')

vers = {
		"ios" : "g-",
        "android" : "y-"
		}

isps = {
		"电信" : "-",
        "联通" : "-",
        "移动" : "-",
        "铁通" : "-",
        "电信通" : "-",
        "教育网" : "-",
		}

for k, v in iter(list(isps.items())):
	view_punch({'os': "ios", 'isp' : k}, v, 321, "ios")

for k, v in iter(list(isps.items())):
	view_punch({'os': "android", 'isp' : k}, v, 322, "android")

for k, v in iter(list(isps.items())):
	view_punch({'os': "", 'isp' : k, 'net' : "3G"}, v, 323, "3G")

for k, v in iter(list(isps.items())):
	view_punch({'os': "", 'isp' : k, 'net' : "wifi"}, v, 324, "wifi")

for k, v in iter(list(isps.items())):
	view_downp2p({'os': "", 'isp' : k, 'net' : "3G"}, v, 325, "3G")

for k, v in iter(list(isps.items())):
	view_downp2p({'os': "", 'isp' : k, 'net' : "wifi"}, v, 326, "wifi")


fig.autofmt_xdate()
plt.show()
