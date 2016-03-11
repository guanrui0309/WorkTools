import matplotlib.pyplot as plt
from dateutil import parser

from get_vod_data import *

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

fig = plt.figure()
fig.canvas.set_window_title('PC');

def view_downp2p(params, fmt):
	
    dates, P2PDownload, P2PRate = get_critical(['Time', 'P2pTotalDown', 'P2pRate'], params)
    dates = [parser.parse(d) for d in dates]

    P2PDownload = [int(float(v))/(1024) for v in P2PDownload]

    plt.subplot(131)

    plt.ylabel("P2P下载量(GB)")
    plt.plot_date(dates, P2PDownload, fmt, label=params['isp'])

    plt.legend(loc='upper left')

    plt.subplot(132)
	
    P2PRate = [float(v)*100 for v in P2PRate]
	
    plt.ylabel("P2P分享率(%)")
    plt.plot_date(dates, P2PRate, fmt, label=params['isp'])


def view_punch(params, fmt):
    dates, PunchSuccRate = get_punch(['Time', 'PunchHoleSucRate'], params)
    dates = [parser.parse(d) for d in dates]

    PunchSuccRate = [float(v)*100 for v in PunchSuccRate]

    plt.subplot(133)

    plt.ylabel("打孔成功率(%)")
    plt.plot_date(dates, PunchSuccRate, fmt, label=params['isp'])

isps = {
		"电信" : "-",
        "联通" : "-",
        "移动" : "-",
        "铁通" : "-",
        "电信通" : "-",
        "教育网" : "-",
		}

for k, v in iter(list(isps.items())):
    view_downp2p({'isp':k}, v)
    view_punch({'isp':k}, v)


fig.autofmt_xdate()
plt.show()
