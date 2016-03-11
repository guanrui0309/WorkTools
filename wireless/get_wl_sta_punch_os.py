import matplotlib.pyplot as plt
from dateutil import parser

from get_wl_data import *

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

def view_punch(params, fmt, column):
    dates, UDTConnSuccRate, PubUDTConnSuccRate, InTCPConnSuccRate, InPunchSuccRate = get_punch(['date', 'UDTConnSuccRate', 'PubUDTConnSuccRate', 'InTCPConnSuccRate', 'InPunchSuccRate'], params)
    dates = [parser.parse(d) for d in dates]

    UDTConnSuccRate = [float(v)*100 for v in UDTConnSuccRate]
    PubUDTConnSuccRate = [float(v)*100 for v in PubUDTConnSuccRate]
    InTCPConnSuccRate = [float(v)*100 for v in InTCPConnSuccRate]
    InPunchSuccRate = [float(v)*100 for v in InPunchSuccRate]

    ax = plt.subplot(421+column)
    ax.set_title(params['os'])
    ax.set_ylim([0, 100])
    plt.ylabel("UDT反连(%)")
    plt.plot_date(dates, UDTConnSuccRate, fmt, label=params['isp'])
    if column == 0:
         plt.legend(loc='upper left', ncol=2)

    ax = plt.subplot(423+column)
    ax.set_ylim([0, 100])
    plt.ylabel("公网UDT直连(%)")
    plt.plot_date(dates, PubUDTConnSuccRate, fmt, label=params['isp'])

    ax = plt.subplot(425+column)
    ax.set_ylim([0, 100])
    plt.ylabel("内网TCP直连(%)")
    plt.plot_date(dates, InTCPConnSuccRate, fmt, label=params['isp'])

    ax = plt.subplot(427+column)
    ax.set_ylim([0, 100])
    plt.ylabel("内网穿透(%)")
    plt.plot_date(dates, InPunchSuccRate, fmt, label=params['isp'])

def view_punch_by_net(net):

	fig = plt.figure()
	fig.canvas.set_window_title('穿透成功率(无线)-按OS分-' + net);
		
	isps = {
			"电信" : "-",
			"联通" : "-",
			"移动" : "-",
			"铁通" : "-",
			"电信通" : "-",
			"教育网" : "-",
			}


	for k, v in iter(list(isps.items())):
		view_punch({'os': "ios", 'net':net, 'isp' : k}, v, 0)

	for k, v in iter(list(isps.items())):
		view_punch({'os': "android", 'net':net, 'isp' : k}, v, 1)


	fig.autofmt_xdate()
	plt.show()


if __name__ == "__main__":
	view_punch_by_net("")