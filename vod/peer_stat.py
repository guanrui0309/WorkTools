import subprocess
import socket
import time

statsd_host = "192.168.199.3"
statsd_port = 8125

inteval_minute = 10

hosts = [
	["119.188.156.37", "pcun", 16],
	["113.105.151.19", "pcdx", 16],
	["119.188.72.149", "flun", 32],
	["122.224.33.105", "fldx", 32],
]

def get_peers_count(host, peerid_size):

    cmd = "mpr_client";
    args = " -host " + host + " -gcid c0fcc7bb20ed4f6378346a506a830f1265e1f262 -file_size 0 -peerid_size " + str(peerid_size)

    out = subprocess.check_output(cmd+args).decode(encoding='utf-8')

    count = 0

    start = out.find("PEERS")
    if start >=0:
        start = out.find("/", start)
        if start >= 0:
            end = out.find(")", start)
            if end >= 0:
                 count = int(out[start+1:end])                        
    

    return count


def to_statsd(s):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(s.encode(encoding='utf-8'), (statsd_host, statsd_port))        

def log_peers_count(h):
	count = get_peers_count(h[0], h[2])
	s = "p2p.statsd.gauge.peers.total_" + h[1] +":"+ str(count) + "|g"
	to_statsd(s)
	print(s)
	

	

while True:

	for h in hosts:
	    log_peers_count(h)
	
	time.sleep(60*inteval_minute)
    

    
    

