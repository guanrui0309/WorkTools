import matplotlib.pyplot as plt
from dateutil import parser

from get_wl_data import *

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  

def view_punch(params, fmt, view):
    dates, UDTConnTimes, PubUDTConnTimes, InTCPConnTimes, InPunchTimes = get_punch(['date', 'UDTConnTimes', 'PubUDTConnTimes', 'InTCPConnTimes', 'InPunchTimes'], params)
    dates = [parser.parse(d) for d in dates]

    ax = plt.subplot(view)
    ax.set_title(params['net'] +  "-" + params['os'])

    if params['net'] == "wifi":
       ax.set_ylim([0, 4*10**9])
    else:
       ax.set_ylim([0, 3*10**7])
	
    plt.plot_date(dates, UDTConnTimes, fmt, label="UDT反连数")
    plt.plot_date(dates, PubUDTConnTimes, fmt, label="公网UDT直连数")
    plt.plot_date(dates, InTCPConnTimes, fmt, label="内网TCP直连数")
    plt.plot_date(dates, InPunchTimes, fmt, label="内网穿透数")

    if view == 221:
         plt.legend(loc='upper left', ncol=2)

def view_conn():

	fig = plt.figure()
	fig.canvas.set_window_title('连接类型(无线)');

	view_punch({'os': "ios", 'net':"wifi"}, "-", 221)
	view_punch({'os': "android", 'net':"wifi"}, "-", 222)
	view_punch({'os': "ios", 'net':"3G"}, "", 223)
	view_punch({'os': "android", 'net':"3G"}, "-", 224)

	fig.autofmt_xdate()
	plt.show()


if __name__ == "__main__":
	view_conn()