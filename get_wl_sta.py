import matplotlib.pyplot as plt
from dateutil import parser

from get_wl_data import *

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

fig = plt.figure()

def view_downp2p(params, fmt):
	
    dates, P2PDownload, P2PRate = get_critical(['date', 'P2PDownload', 'P2PRate'], params)
    dates = [parser.parse(d) for d in dates]

    P2PDownload = [int(float(v))/(1024) for v in P2PDownload]

    plt.subplot(321)
    plt.ylabel("P2P下载量(GB)")
    plt.plot_date(dates, P2PDownload, fmt, label=params['os'])
    plt.legend(loc='upper left')
	
    P2PRate = [float(v)*100 for v in P2PRate]

    plt.subplot(322)
    plt.ylabel("P2P分享率(%)")
    plt.plot_date(dates, P2PRate, fmt, label=params['os'])



def view_playfeel(params, fmt):
    dates, EachFstBufTm, EachStopQuitTm = get_playfeel(['date', 'EachFstBufTm', 'EachStopQuitTm'], params)
    dates = [parser.parse(d) for d in dates]

    plt.subplot(323)
    plt.ylabel("首缓冲时间(s)")
    plt.plot_date(dates, EachFstBufTm, fmt, label=params['os'])

    plt.subplot(324)
    plt.ylabel("初次流畅观看时长(s)")
    plt.plot_date(dates, EachStopQuitTm, fmt, label=params['os'])

def view_mplay(params, fmt):
    dates, EachStartP2pOKTm = get_mplay(['date', 'EachStartP2pOKTm'], params)
    dates = [parser.parse(d) for d in dates]

    EachStartP2pOKTm = [float(v)*100 for v in EachStartP2pOKTm]

    plt.subplot(325)
    plt.ylabel("播放成功率(%)")
    plt.plot_date(dates, EachStartP2pOKTm, fmt, label=params['os'])

def view_punch(params, fmt):
    dates, PunchSuccRate = get_punch(['date', 'PunchSuccRate'], params)
    dates = [parser.parse(d) for d in dates]

    PunchSuccRate = [float(v)*100 for v in PunchSuccRate]

    plt.subplot(326)
    plt.ylabel("打孔成功率(%)")
    plt.plot_date(dates, PunchSuccRate, fmt, label=params['isp'])
    plt.legend(loc='upper left')

vers = {
		"ios" : "g-",
        "android" : "y-"
		}

for k, v in iter(list(vers.items())):
    view_downp2p({'os' : k}, v)
    view_playfeel({'os' : k}, v)
    view_mplay({'os' : k}, v)
	
isps = {
		"电信" : "-",
        "联通" : "-",
        "移动" : "-",
        "铁通" : "-",
        "电信通" : "-",
        "教育网" : "-",
		}
		
for k, v in iter(list(isps.items())):
	view_punch({'os': "", 'isp' : k}, v)


fig.autofmt_xdate()
plt.show()
