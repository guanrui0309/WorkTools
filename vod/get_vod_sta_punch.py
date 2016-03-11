import matplotlib.pyplot as plt
from dateutil import parser

from get_vod_data import *

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

fig = plt.figure()
fig.canvas.set_window_title('穿透成功率(PC)');

def view_punch(params, fmt):
    dates, UdtConnSucRate, UdpBroConnSucRate, PunchHoleSucRate, TotalPunchHoleSucRate = get_punch(['Time', 'UdtConnSucRate', 'UdpBroConnSucRate', 'PunchHoleSucRate', 'TotalPunchHoleSucRate'], params)
    dates = [parser.parse(d) for d in dates]

    UdtConnSucRate = [float(v)*100 for v in UdtConnSucRate]
    UdpBroConnSucRate = [float(v)*100 for v in UdpBroConnSucRate]
    PunchHoleSucRate = [float(v)*100 for v in PunchHoleSucRate]
    TotalPunchHoleSucRate = [float(v)*100 for v in TotalPunchHoleSucRate]

    ax = plt.subplot(411)
    ax.set_ylim([0, 100])
    plt.ylabel("UDT反连(%)")
    plt.plot_date(dates, UdpBroConnSucRate, fmt, label=params['isp'])
    plt.legend(loc='upper left', ncol=2)

    ax = plt.subplot(412)
    ax.set_ylim([0, 100])
    plt.ylabel("UDT直连(%)")
    plt.plot_date(dates, UdtConnSucRate, fmt, label=params['isp'])

    ax = plt.subplot(414)
    ax.set_ylim([0, 100])
    plt.ylabel("内网穿透(%)")
    plt.plot_date(dates, PunchHoleSucRate, fmt, label=params['isp'])

    '''
    ax = plt.subplot(414)
    ax.set_ylim([0, 100])
    plt.ylabel("打孔成功率(%)")
    plt.plot_date(dates, TotalPunchHoleSucRate, fmt, label=params['isp'])
    '''
	
isps = {
		"电信": "-",
        "联通": "-",
        "移动": "-",
        "铁通": "-",
        "电信通": "-",
        "教育网": "-",
		}


for k, v in iter(list(isps.items())):
	view_punch({'os': "", 'isp' : k}, v)

fig.autofmt_xdate()
plt.show()
