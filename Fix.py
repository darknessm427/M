V=8
import urllib.request
import urllib.parse
from urllib.parse import quote
import os
try:
    import requests
except ImportError:
    print("Requests module not installed. Installing now...")
    os.system('pip install requests')
try:
    import requests
except ModuleNotFoundError:
    os.system('wget https: //github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
try:
    import requests
except ModuleNotFoundError:
    os.system('curl -L -o requests-2.32.2.tar.gz https: //github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz')
    os.system('tar -xzvf requests-2.32.2.tar.gz')
    os.chdir('requests-2.32.2')
    os.system('python setup.py install')
    import requests
import re
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
try:
    import rich
except Exception:
    print("Rich module not installed. Installing now...")
    os.system('pip install rich')
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich.table import Table
try:
    import retrying
except Exception:
    print("retrying module not installed. Installing now...")
    os.system('pip install retrying')
try:
    import retrying
except Exception:
    os.system("wget https://github.com/rholder/retrying/archive/refs/tags/v1.3.3.tar.gz")
    os.system("tar -zxvf v1.3.3.tar.gz")
    os.chdir("retrying-1.3.3")
    os.system("python setup.py install")
from retrying import retry
from requests.exceptions import ConnectionError

import random
import subprocess
import json
import sys


console = Console()
wire_config_temp=''
wire_c=1
wire_p=0
send_msg_wait=0
results = []
save_result=[]
best_result=[]
WoW_v2=''
isIran=''
max_workers_number=0

def info():
    console.clear()
    
    table = Table(show_header=True,title="Info", header_style="bold blue")
    table.add_column("Creator", width=15)
    
    table.add_column("contact", justify="right")
    table.add_row("arshiacomplus",
"1 - Telegram")
    table.add_row("arshiacomplus",
"2 - github")
    console.print(table)
    
    print('\nEnter a Number\n')
    options2={
  "1": "open Telegram Channel",
  "2": "open github ",
  "0": "Exit"
}
    for key, value in options2.items():
    	rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats2 = Prompt.ask("Choose an option", choices=list(options2.keys()), default="1")
    
    if whats2=='0':
    	os.execv(sys.executable,
['python'
] + sys.argv)
    elif whats2=='1':
    	os.system("termux-open-url 'https://t.me/arshia_mod_fun'")
    elif whats2=='2'   :
    	os.system("termux-open-url 'https://github.com/darknessm427/WarpScanner/tree/main'")
    	
def check_ipv6():
    
    try:
    	ipv6 = requests.get('http: //v6.ipv6-test.com/api/myip.php')
    	if ipv6.status_code == 200:
    		ipv6 ="[green]Available[/green]"
    except Exception:
    	ipv6 = "Unavailable"
    try:
    	ipv4 = requests.get('http: //v4.ipv6-test.com/api/myip.php')
    	if ipv4.status_code == 200:
    		ipv4= "[green]Available[/green]"
    except Exception:
    	ipv4 = "Unavailable"
    return  [ipv4,ipv6
]

def input_p(pt ,options):
    os.system('clear')
    options.update({
  "0": "Exit"
})
    print(pt)
    for key, value in options.items():
    	rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    whats = Prompt.ask("Choose an option", choices=list(options.keys()), default="1")
    if whats=='0':
    	os.execv(sys.executable,
['python'
] + sys.argv)
    return whats
def urlencode(string):
    
    if string is None:
        return None
    return urllib.parse.quote(string, safe='a-zA-Z0-9.~_-')

def fetch_config_from_api():

    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
    	    try:
    	    	response = urllib.request.urlopen("https://api.zeroteam.top/warp?format=sing-box", timeout=30).read().decode('utf-8')
    	    	return response
    	    except Exception:
    	    	response = requests.get("https://api.zeroteam.top/warp?format=sing-box", timeout=30)
    	    	return response.text
    	    
    response = file_o()
    data = json.loads(response)
    return {
        'PrivateKey': data.get('private_key'),
        'PublicKey': data.get('peer_public_key'),
        'Reserved': ','.join([str(x) for x in data.get('reserved',
    [])
  ]) if data.get('reserved') else None,
        'Address': data.get('local_address')
}
    
def free_cloudflare_account2():
    
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
    	    try:
    	    	response = urllib.request.urlopen("https://fscarmen.cloudflare.now.cc/wg", timeout=30).read().decode('utf-8')
    	    	return response
    	    except Exception:
    	    	response = requests.get("https://fscarmen.cloudflare.now.cc/wg", timeout=30)
    	    	return response.text
    	    
    response = file_o()
    PublicKey=response[response.index(':')+2:response.index('\n')
]
    PrivateKey=response[response.index('\n')+13:
]
    reserved=[
  222,
  6,
  184
]
    return [
  "2606:4700:110:8d48:52cb:c565:3a80:c416/128", PrivateKey , reserved, PublicKey
]

def free_cloudflare_account():

    	
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
    	    try:
    	    	response = urllib.request.urlopen("https://api.zeroteam.top/warp?format=sing-box", timeout=30).read().decode('utf-8')
    	    	return response
    	    except Exception:
    	    	response = requests.get("https://api.zeroteam.top/warp?format=sing-box", timeout=30)
    	    	return response.text
    try:
            output = file_o()
    except ConnectionError:
            console.print("[bold red]Failed to connect to API after 6 attempts.[/bold red]")

       
    Address_pattern = r'"2606:4700:[0-9a-f:]+/128"'
    private_key_pattern = r'"private_key": "[0-9a-zA-Z/+]+="'
    reserved_pattern = r'"reserved": [
  [
    0-9
  ]+(,
  [
    0-9
  ]+){
    2
  }
]'

    Address_search = re.search(Address_pattern, output)
    private_key_search = re.search(private_key_pattern, output)
    reserved_search = re.search(reserved_pattern, output)

      
    Address_key = Address_search.group(0).replace('"', '') if Address_search else None
    private_key = private_key_search.group(0).split(':')[
  1
].replace('"', '') if private_key_search else None
    reserved = reserved_search.group(0).replace('"reserved":', '').replace('"', '') if reserved_search else None

    all_key=[Address_key , private_key , reserved,
  "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo="
]
    return all_key
def upload_to_bashupload(config_data):
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda x: isinstance(x, ConnectionError))
    def file_o():
    	files = {'file': ('output.json', config_data)
}
    	try:
    		response = requests.post('https: //bashupload.com/', files=files, timeout=30)
    	except Exception:
    		response = requests.post('https: //bashupload.com/', files=files, timeout=50)
    	return response
    try:
        
        response = file_o()

        if response.ok:
            download_link = response.text.strip()
            download_link_with_query = download_link[
  59:len(download_link)-27
] + "?download=1"
            console.print(f'[green
]Your link: {download_link_with_query
}[/green
]')
        else:
            console.print("[red]Something happened with creating the link[/red]", style="bold red")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]", style="bold red")


    
def create_ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start[
  :
]
    ip_range = []

    while temp != end:
        ip_range.append('.'.join(map(str, temp)))
        temp[
  3
] += 1
        for i2 in (3,
2,
1):
            if temp[i2
] == 256:
                temp[i2
] = 0
                temp[i2-1
] += 1
    ip_range.append(end_ip)
    return ip_range
def scan_ip_port(ip, port, results, packet_loss):
    global best_result
    
   
    start_time = time.time() 
    try:
      
        ping_command = [
  "ping",
  "-c",
  "1",
  "-w",
  "5",
  "-p", str(port), ip
]

        
        process = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

     
        while process.poll() is None:
            if time.time() - start_time > 5:
                process.terminate()  
                break
            time.sleep(0.1)  
        output, error = process.communicate()
       
        if process.returncode == 0:
            
            ping_time = float(output.decode().split('time=')[
  1
].split(' ')[
  0
])
            results.append((ip, port, ping_time))


            
        else:
           
            console.print(f"IP: {ip} Port: {port} is not responding or closed.", style="red")
            packet_loss[ip
] = packet_loss.get(ip,
0) + 100

        	

    except Exception as E:
        console.print(f"Error - {E}", style="red")
        
def main_v6():
    def generate_ipv6():
        return f"2606:4700:d{random.randint(0, 1)}::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"

    def ping_ip(ip, port):
        try:
            output = subprocess.check_output([
  "ping6",
  "-c",
  "4",
  "-p", str(port), ip
], text=True)
            for line in output.splitlines():
                if "min/avg/max" in line:
                    parts = line.split()
                    avg_ping_time = parts[
  3
].split('/')[
  1
]
                    return float(avg_ping_time)
        except subprocess.CalledProcessError:
            return float('inf')

    def scan_ip(ip, ports_to_check):
        results = []
        for n in ports_to_check:
            ping_time = ping_ip(ip, n)
            results.append((ip, ping_time))
        return results

    console = Console()
    ports_to_check = [
  1074,
  864
]
    best_ping = float("inf")
    best_ip = ""
    random_ip=""

    table = Table(title="IP Scan Results")
    table.add_column("IP Address", justify="center", style="cyan", no_wrap=True)
    table.add_column("Ping Time (ms)", justify="center", style="green")

    results = []
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(scan_ip, generate_ipv6(), ports_to_check) for _ in range(100)
]
        for future in as_completed(futures):
            results.extend(future.result())

    # Sort the results based on ping time
    results.sort(key=lambda x: x[
  1
])

    for ip, ping_time in results:
        table.add_row(ip,  f"{ping_time:.2f}")
        if ping_time < best_ping:
            best_ping = ping_time
            best_ip = ip

    console.print(table)
    port_random = ports_to_check[random.randint(0, len(ports_to_check) - 1)
]
    if best_ip:
        console.print(f"\n[bold green]Best IP : [{best_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        best_ip_mix = [
  1
] * 2
        best_ip_mix[
  0
] = "[" + best_ip + "]"
        best_ip_mix[
  1
] = port_random
        return best_ip_mix
    else:
        console.print(f"\n[bold green]Best IP : [{random_ip}]:{port_random} with ping time: {best_ping} ms[/bold green]")
        best_ip_mix = [
  1
] * 2
        best_ip_mix[
  0
] = "[" + random_ip + "]"
        best_ip_mix[
  1
] = port_random
        return best_ip_mix

def main():
    global save_result
    global max_workers_number

    if what!='0':
        which_v=input_p('Choose an ip version\n ',
{
  "1": 'ipv4' ,
  "2": 'ipv6'
})
        if which_v=="2":
            console.clear()
            
            best_result=main_v6()
            return best_result
    Cpu_speed=input_p('scan power',
{
  "1": "Faster",
  "2": "Slower"
})
    if Cpu_speed == "1": max_workers_number=1000
    elif Cpu_speed == "2": max_workers_number=500
    
    console.clear()
    console.print("Please wait, scanning IP ...", style="blue")

    start_ips = [
  "188.114.96.0",
  "162.159.192.0",
  "162.159.195.0"
]
    end_ips = [
  "188.114.99.224",
  "162.159.193.224",
  "162.159.195.224"
]
    ports = [
  1074,
  894,
  908,
  878
]
    results = []
    packet_loss = {}

    for start_ip, end_ip in zip(start_ips, end_ips):
        ip_range = create_ip_range(start_ip, end_ip)
        with ThreadPoolExecutor(max_workers=max_workers_number) as executor:
            for ip in ip_range:
                for port in ports:
                    executor.submit(scan_ip_port, ip, port, results, packet_loss)

    for ip in packet_loss:
        packet_loss[ip
] = (packet_loss[ip
] / len(ports)) * 100
        
        

    extended_results = []
    for result in results:
        ip, port, ping = result
        loss_rate = packet_loss.get(ip,
0)
        if loss_rate == 0.00 and ping > 250.00:
            try:
                save_result.index(str(ip))
            except Exception:
                save_result.append("\n")
                save_result.append(str(ip))
        combined_score = ping + (loss_rate * 10)
        extended_results.append((ip, port, ping, loss_rate, combined_score))
    
  
    for ip in packet_loss:
        if ip not in [res[
    0
  ] for res in extended_results
]:
            loss_rate = packet_loss[ip
]
            
            extended_results.append((ip, None, None, loss_rate, loss_rate * 10))

    sorted_results = sorted(extended_results, key=lambda x: x[
  4
])

   
    while len(sorted_results) < 10:
        sorted_results.append(("No IP", None, None,
100,
1000))

    console.clear()
    table = Table(show_header=True,title="IP Scan Results", header_style="bold blue")
    table.add_column("IP", style="dim", width=15)
    table.add_column("Port", justify="right")
    table.add_column("Ping (ms)", justify="right")
    table.add_column("Packet Loss (%)", justify="right")
    table.add_column("Score", justify="right")

    for ip, port, ping, loss_rate, combined_score in sorted_results[
  : 10
]:
        table.add_row(ip, str(port) if port else "878", f"{ping:.2f}" if ping else "None", f"{loss_rate:.2f}%", f"{combined_score:.2f}")

    console.print(table)

    best_result = sorted_results[
  0
] if sorted_results else None
    if best_result and best_result[
  0
] != "No IP":
        ip, port, ping, loss_rate, combined_score = best_result
        try:
            console.print(f"The best IP: {ip}:{port if port else 'N/A'} , ping: {ping:.2f} ms, packet loss: {loss_rate:.2f}%, score: {combined_score:.2f}", style="green")
        except TypeError:
            console.print(f"The best IP: {ip}:{port if port else '878'} , ping: None, packet loss: {loss_rate:.2f}%, score: {combined_score:.2f}", style="green")
        best_result=2*[
  1
]
        best_result[
  0
]=f"{ip}"
        best_result[
  1
]=878
    else:
        console.print("Nothing was found", style="red")
    t=False
    if what == '1':
        if do_you_save=='1':
            if which =="1":
                 with open('/storage/emulated/0/result.csv' ,
"w") as f:
                      for j in save_result[
  1:
]:
                          if j != "\n":
                              f.write(j)
                              t=False
                          else:
                         # 	if j != save_result[len(save_result)-1
]:
                          	    if t==False:
                          	    	 f.write(",")
                          	    t=True
                          	   
            else:
                 with open('/storage/emulated/0/result.csv' ,
"w") as f:
                      for j in save_result:
                          f.write(j)
                       
            print(' saved in /storage/emulated/0/result.csv !')
            

    return best_result


def main2():
    global best_result
    
    
    def main2_2():
    	global WoW_v2
    	try:
    	   all_key=free_cloudflare_account()
    	except Exception as E:
            print(' Try again Error =', E)
            exit()

    	try:
            	all_key2=free_cloudflare_account()
    	except Exception as E:
            	print(' Try again Error =', E)
            	exit()
    	os.system('clear')
    	print(f'Make Wireguard ')    	
    	WoW_v2+=f'''
    {
  {
    "remarks": "ÐΛɌ₭ᑎΞ𐒡𐒡 - WoW",
    "log": {
      {
        "loglevel": "warning"
      }
    },
    "dns": {
      {
        "hosts": {
          {
            "geosite:category-ads-all": "127.0.0.1",
            "geosite:category-ads-ir": "127.0.0.1"'''
    	if polrn_block=='1' :WoW_v2+=f''',
            "geosite:category-porn": "127.0.0.1"'''
                
    	WoW_v2+=f'''
          }
        },
        "servers": [
          "https://94.140.14.14/dns-query",
          {
            {
              "address": "8.8.8.8",
              "domains": [
                "geosite:category-ir",
                "domain:.ir"
              ],
              "expectIPs": [
                "geoip:ir"
              ],
              "port": 53
            }
          }
        ],
        "tag": "dns"
      }
    },
    "inbounds": [
      {
        {
          "port": 10808,
          "protocol": "socks",
          "settings": {
            {
              "auth": "noauth",
              "udp": true,
              "userLevel": 8
            }
          },
          "sniffing": {
            {
              "destOverride": [
                "http",
                "tls"
              ],
              "enabled": true,
              "routeOnly": true
            }
          },
          "tag": "socks-in"
        }
      },
      {
        {
          "port": 10809,
          "protocol": "http",
          "settings": {
            {
              "auth": "noauth",
              "udp": true,
              "userLevel": 8
            }
          },
          "sniffing": {
            {
              "destOverride": [
                "http",
                "tls"
              ],
              "enabled": true,
              "routeOnly": true
            }
          },
          "tag": "http-in"
        }
      },
      {
        {
          "listen": "127.0.0.1",
          "port": 10853,
          "protocol": "dokodemo-door",
          "settings": {
            {
              "address": "1.1.1.1",
              "network": "tcp,udp",
              "port": 53
            }
          },
          "tag": "dns-in"
        }
      }
    ],
    "outbounds": [
      {
        {
          "protocol": "wireguard",
          "settings": {
            {
              "address": [
                "172.16.0.2/32",
                "{all_key[0]}"
              ],
              "mtu": 1280,
              "peers": [
                {
                  {
                    "endpoint": "{best_result[0]}:{best_result[1]}",
                    "publicKey": "{all_key[3]}"
                  }
                }
              ],
              "reserved": {all_key[
                  2
                ]
              },
              "secretKey": "{all_key[1]}",
              "keepAlive": 10
            }
          },
          "streamSettings": {
            {
              "sockopt": {
                {
                  "dialerProxy": "warp-ir"
                }
              }
            }
          },
          "tag": "warp-out"
        }
      },
      {
        {
          "protocol": "wireguard",
          "settings": {
            {
              "address": [
                "172.16.0.2/32",
                "{all_key2[0]}"
              ],
              "mtu": 1280,
              "peers": [
                {
                  {
                    "endpoint": "162.159.192.115:864",
                    "publicKey": "{all_key2[3]}"
                  }
                }
              ],
              "reserved": {all_key2[
                  2
                ]
              },
              "secretKey": "{all_key2[1]}",
              "keepAlive": 10
            }
          },
          "tag": "warp-ir"
        }
      },
      {
        {
          "protocol": "dns",
          "tag": "dns-out"
        }
      },
      {
        {
          "protocol": "freedom",
          "settings": {
            {}
          },
          "tag": "direct"
        }
      },
      {
        {
          "protocol": "blackhole",
          "settings": {
            {
              "response": {
                {
                  "type": "http"
                }
              }
            }
          },
          "tag": "block"
        }
      }
    ],
    "policy": {
      {
        "levels": {
          {
            "8": {
              {
                "connIdle": 300,
                "downlinkOnly": 1,
                "handshake": 4,
                "uplinkOnly": 1
              }
            }
          }
        },
        "system": {
          {
            "statsOutboundUplink": true,
            "statsOutboundDownlink": true
          }
        }
      }
    },
    "routing": {
      {
        "domainStrategy": "IPIfNonMatch",
        "rules": [
          {
            {
              "inboundTag": [
                "dns-in"
              ],
              "outboundTag": "dns-out",
              "type": "field"
            }
          },
          {
            {
              "ip": [
                "8.8.8.8"
              ],
              "outboundTag": "direct",
              "port": "53",
              "type": "field"
            }
          },
          {
            {
              "domain": [
                "geosite:category-ir",
                "domain:.ir"
              ],
              "outboundTag": "direct",
              "type": "field"
            }
          },
          {
            {
              "ip": [
                "geoip:ir",
                "geoip:private"
              ],
              "outboundTag": "direct",
              "type": "field"
            }
          },
          {
            {
              "domain": [
                "geosite:category-ads-all",
                "geosite:category-ads-ir"'''
    	if polrn_block=='1' :WoW_v2+=f''',
                "geosite:category-porn"'''
    	WoW_v2+=f'''
              ],
              "outboundTag": "block",
              "type": "field"
            }
          },
          {
            {
              "outboundTag": "warp-out",
              "type": "field",
              "network": "tcp,udp"
            }
          }
        ]
      }
    },
    "stats": {
      {}
    }
  }
},
{
  {
    "remarks": "ÐΛɌ₭ᑎΞ𐒡𐒡 - Warp",
    "log": {
      {
        "loglevel": "warning"
      }
    },
    "dns": {
      {
        "hosts": {
          {
            "geosite:category-ads-all": "127.0.0.1",
            "geosite:category-ads-ir": "127.0.0.1"'''
    	if polrn_block=='1' :WoW_v2+=f''',
            "geosite:category-porn": "127.0.0.1"'''
                
    	WoW_v2+=f'''
          }
        },
        "servers": [
          "https://94.140.14.14/dns-query",
          {
            {
              "address": "8.8.8.8",
              "domains": [
                "geosite:category-ir",
                "domain:.ir"
              ],
              "expectIPs": [
                "geoip:ir"
              ],
              "port": 53
            }
          }
        ],
        "tag": "dns"
      }
    },
    "inbounds": [
      {
        {
          "port": 10808,
          "protocol": "socks",
          "settings": {
            {
              "auth": "noauth",
              "udp": true,
              "userLevel": 8
            }
          },
          "sniffing": {
            {
              "destOverride": [
                "http",
                "tls"
              ],
              "enabled": true,
              "routeOnly": true
            }
          },
          "tag": "socks-in"
        }
      },
      {
        {
          "port": 10809,
          "protocol": "http",
          "settings": {
            {
              "auth": "noauth",
              "udp": true,
              "userLevel": 8
            }
          },
          "sniffing": {
            {
              "destOverride": [
                "http",
                "tls"
              ],
              "enabled": true,
              "routeOnly": true
            }
          },
          "tag": "http-in"
        }
      },
      {
        {
          "listen": "127.0.0.1",
          "port": 10853,
          "protocol": "dokodemo-door",
          "settings": {
            {
              "address": "1.1.1.1",
              "network": "tcp,udp",
              "port": 53
            }
          },
          "tag": "dns-in"
        }
      }
    ],
    "outbounds": [
      {
        {
          "protocol": "wireguard",
          "settings": {
            {
              "address": [
                "172.16.0.2/32",
                "{all_key[0]}"
              ],
              "mtu": 1280,
              "peers": [
                {
                  {
                    "endpoint": "{best_result[0]}:{best_result[1]}",
                    "publicKey": "{all_key[3]}"
                  }
                }
              ],
              "reserved": {all_key[
                  2
                ]
              },
              "secretKey": "{all_key[1]}",
              "keepAlive": 10
            }
          },
          "tag": "warp"
        }
      },
      {
        {
          "protocol": "dns",
          "tag": "dns-out"
        }
      },
      {
        {
          "protocol": "freedom",
          "settings": {
            {}
          },
          "tag": "direct"
        }
      },
      {
        {
          "protocol": "blackhole",
          "settings": {
            {
              "response": {
                {
                  "type": "http"
                }
              }
            }
          },
          "tag": "block"
        }
      }
    ],
    "policy": {
      {
        "levels": {
          {
            "8": {
              {
                "connIdle": 300,
                "downlinkOnly": 1,
                "handshake": 4,
                "uplinkOnly": 1
              }
            }
          }
        },
        "system": {
          {
            "statsOutboundUplink": true,
            "statsOutboundDownlink": true
          }
        }
      }
    },
    "routing": {
      {
        "domainStrategy": "IPIfNonMatch",
        "rules": [
          {
            {
              "inboundTag": [
                "dns-in"
              ],
              "outboundTag": "dns-out",
              "type": "field"
            }
          },
          {
            {
              "ip": [
                "8.8.8.8"
              ],
              "outboundTag": "direct",
              "port": "53",
              "type": "field"
            }
          },
          {
            {
              "domain": [
                "geosite:category-ir",
                "domain:.ir"
              ],
              "outboundTag": "direct",
              "type": "field"
            }
          },
          {
            {
              "ip": [
                "geoip:ir",
                "geoip:private"
              ],
              "outboundTag": "direct",
              "type": "field"
            }
          },
          {
            {
              "domain": [
                "geosite:category-ads-all",
                "geosite:category-ads-ir"'''
    	if polrn_block=='1' :WoW_v2+=f''',
                "geosite:category-porn"'''
    	WoW_v2+=f'''
              ],
              "outboundTag": "block",
              "type": "field"
            }
          },
          {
            {
              "outboundTag": "warp",
              "type": "field",
              "network": "tcp,udp"
            }
          }
        ]
      }
    },
    "stats": {
      {}
    }
  }
}'''
    	if n !=how_many-1:
    		WoW_v2+=','
    		return 
    def main2_1():
        global best_result
        
        print()
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        if what == '7':
            if isIran=='2' :
            	try:
            		all_key2=free_cloudflare_account()
            	except Exception as E:
            		print(' Try again Error =', E)
            		exit()
        else:
            	try:
            		all_key2=free_cloudflare_account()
            	except Exception as E:
            		print(' Try again Error =', E)
            		exit()

        
        temp_ip=''
        temp_port=''
        temp_c=0
        if what =='3':
            print("\033[0m")
            enter_ip=input('Enter ip with port(Default =Enter( N )) : ')
            if enter_ip=='N' or  enter_ip=='n':
                best_result=[
  "162.159.195.166",
  908
]
            else:
                while enter_ip[temp_c
] !=':':
                        temp_ip=temp_ip+enter_ip[temp_c
]
                        temp_c=temp_c+1
                            
                        
                set_enter_ip=enter_ip.index(":")
                temp_port=enter_ip[set_enter_ip+1:
]
                    

                    
                    
                    #temp_port=temp_port+enter_ip[i
]
                best_result=[temp_ip, int(temp_port)
]

        Wow=''
        if what=='7':
        	 print("\033[0m")
        	 os.system('clear')
        	 
        	 Wow=f'''{
  {
    "dns": {
      {
        "hosts": {
          {
            "geosite:category-ads-all": "127.0.0.1",
            "geosite:category-ads-ir": "127.0.0.1"'''
        	 if polrn_block=='1' : Wow+=''',
            "geosite:category-porn": "127.0.0.1"'''
        
        	
        	 if isIran=='1' :Wow+=f'''
          }
        },
        "servers": [
          "https://94.140.14.14/dns-query",
          {
            {
              "address": "8.8.8.8",
              "domains": [
                "geosite:category-ir",
                "domain:.ir"
              ],
              "expectIPs": [
                "geoip:ir"
              ],
              "port": 53
            }
          }
        ],
        "tag": "dns"
      }
    },
    "inbounds": [
      {
        {
          "port": 10808,
          "protocol": "socks",
          "settings": {
            {
              "auth": "noauth",
              "udp": true,
              "userLevel": 8
            }
          },
          "sniffing": {
            {
              "destOverride": [
                "http",
                "tls"
              ],
              "enabled": true
            }
          },
          "tag": "socks-in"
        }
      },
      {
        {
          "port": 10809,
          "protocol": "http",
          "settings": {
            {
              "auth": "noauth",
              "udp": true,
              "userLevel": 8
            }
          },
          "sniffing": {
            {
              "destOverride": [
                "http",
                "tls"
              ],
              "enabled": true
            }
          },
          "tag": "http-in"
        }
      },
      {
        {
          "listen": "127.0.0.1",
          "port": 10853,
          "protocol": "dokodemo-door",
          "settings": {
            {
              "address": "1.1.1.1",
              "network": "tcp,udp",
              "port": 53
            }
          },
          "tag": "dns-in"
        }
      }
    ],
    "log": {
      {
        "loglevel": "warning"
      }
    },
    "outbounds": [
      {
        {
          "protocol": "wireguard",
          "settings": {
            {
              "address": [
                "172.16.0.2/32",
                "{all_key[0]}"
              ],
              "mtu": 1280,
              "peers": [
                {
                  {
                    "endpoint": "{best_result[0]}:{best_result[1]}",
                    "publicKey": "{all_key[3]}"
                  }
                }
              ],
              "reserved": {all_key[
                  2
                ]
              },
              "secretKey": "{all_key[1]}"
            }
          },
          "tag": "warp"
        }
      },
      {
        {
          "protocol": "dns",
          "tag": "dns-out"
        }
      },
      {
        {
          "protocol": "freedom",
          "settings": {
            {}
          },
          "tag": "direct"
        }
      },
      {
        {
          "protocol": "blackhole",
          "settings": {
            {
              "response": {
                {
                  "type": "http"
                }
              }
            }
          },
          "tag": "block"
        }
      }
    ],
    "policy": {
      {
        "levels": {
          {
            "8": {
              {
                "connIdle": 300,
                "downlinkOnly": 1,
                "handshake": 4,
                "uplinkOnly": 1
              }
            }
          }
        },
        "system": {
          {
            "statsOutboundUplink": true,
            "statsOutboundDownlink": true
          }
        }
      }
    },
    "remarks": "ÐΛɌ₭ᑎΞ𐒡𐒡 - Warp",
    "routing": {
      {
        "domainStrategy": "IPIfNonMatch",
        "rules": [
          {
            {
              "inboundTag": [
                "dns-in"
              ],
              "outboundTag": "dns-out",
              "type": "field"
            }
          },
          {
            {
              "ip": [
                "8.8.8.8"
              ],
              "outboundTag": "direct",
              "port": "53",
              "type": "field"
            }
          },
          {
            {
              "domain": [
                "geosite:category-ir",
                "domain:.ir"
              ],
              "outboundTag": "direct",
              "type": "field"
            }
          },
          {
            {
              "ip": [
                "geoip:ir",
                "geoip:private"
              ],
              "outboundTag": "direct",
              "type": "field"
            }
          },
          {
            {
              "domain": [
                "geosite:category-ads-all",
                "geosite:category-ads-ir"'''
        	 
        	 if isIran=='1':
        	 	if polrn_block=='1':Wow+=''',
                "geosite:category-porn"'''
        	 	Wow+='''
              ],
              "outboundTag": "block",
              "type": "field"
            },
            {
              "network": "tcp,udp",
              "outboundTag": "warp",
              "type": "field"
            }
          ]
        },
        "stats": {}
      }'''
        	 if isIran == '2' : Wow+=f'''
    }
  },
  "servers": [
    "https://94.140.14.14/dns-query",
    {
      {
        "address": "8.8.8.8",
        "domains": [
          "geosite:category-ir",
          "domain:.ir"
        ],
        "expectIPs": [
          "geoip:ir"
        ],
        "port": 53
      }
    }
  ],
  "tag": "dns"
}
},
"inbounds": [
{
  {
    "port": 10808,
    "protocol": "socks",
    "settings": {
      {
        "auth": "noauth",
        "udp": true,
        "userLevel": 8
      }
    },
    "sniffing": {
      {
        "destOverride": [
          "http",
          "tls"
        ],
        "enabled": true
      }
    },
    "tag": "socks-in"
  }
},
{
  {
    "port": 10809,
    "protocol": "http",
    "settings": {
      {
        "auth": "noauth",
        "udp": true,
        "userLevel": 8
      }
    },
    "sniffing": {
      {
        "destOverride": [
          "http",
          "tls"
        ],
        "enabled": true
      }
    },
    "tag": "http-in"
  }
},
{
  {
    "listen": "127.0.0.1",
    "port": 10853,
    "protocol": "dokodemo-door",
    "settings": {
      {
        "address": "1.1.1.1",
        "network": "tcp,udp",
        "port": 53
      }
    },
    "tag": "dns-in"
  }
}
],
"log": {
{
  "loglevel": "warning"
}
},
"outbounds": [
{
  {
    "protocol": "wireguard",
    "settings": {
      {
        "address": [
          "172.16.0.2/32",
          "{all_key[0]}"
        ],
        "mtu": 1280,
        "peers": [
          {
            {
              "endpoint": "{best_result[0]}:{best_result[1]}",
              "publicKey": "{all_key[3]}"
            }
          }
        ],
        "reserved": {all_key[
            2
          ]
        },
        "secretKey": "{all_key[1]}"
      }
    },
    "streamSettings": {
      {
        "network": "tcp",
        "security": "",
        "sockopt": {
          {
            "dialerProxy": "warp-ir"
          }
        }
      }
    },
    "tag": "warp-out"
  }
},
{
  {
    "protocol": "wireguard",
    "settings": {
      {
        "address": [
          "172.16.0.2/32",
          "{all_key2[0]}"
        ],
        "mtu": 1280,
        "peers": [
          {
            {
              "endpoint": "{best_result[0]}:{best_result[1]}",
              "publicKey": "{all_key[3]}"
            }
          }
        ],
        "reserved": {all_key2[
            2
          ]
        },
        "secretKey": "{all_key2[1]}"
      }
    },
    "tag": "warp-ir"
  }
},
{
  {
    "protocol": "dns",
    "tag": "dns-out"
  }
},
{
  {
    "protocol": "freedom",
    "settings": {
      {}
    },
    "tag": "direct"
  }
},
{
  {
    "protocol": "blackhole",
    "settings": {
      {
        "response": {
          {
            "type": "http"
          }
        }
      }
    },
    "tag": "block"
  }
}
],
"policy": {
{
  "levels": {
    {
      "8": {
        {
          "connIdle": 300,
          "downlinkOnly": 1,
          "handshake": 4,
          "uplinkOnly": 1
        }
      }
    }
  },
  "system": {
    {
      "statsOutboundUplink": true,
      "statsOutboundDownlink": true
    }
  }
}
},
"remarks": " ÐΛɌ₭ᑎΞ𐒡𐒡 - WoW",
"routing": {
{
  "domainStrategy": "IPIfNonMatch",
  "rules": [
    {
      {
        "inboundTag": [
          "dns-in"
        ],
        "outboundTag": "dns-out",
        "type": "field"
      }
    },
    {
      {
        "ip": [
          "8.8.8.8"
        ],
        "outboundTag": "direct",
        "port": "53",
        "type": "field"
      }
    },
    {
      {
        "domain": [
          "geosite:category-ir",
          "domain:.ir"
        ],
        "outboundTag": "direct",
        "type": "field"
      }
    },
    {
      {
        "ip": [
          "geoip:ir",
          "geoip:private"
        ],
        "outboundTag": "direct",
        "type": "field"
      }
    },
    {
      {
        "domain": [
          "geosite:category-ads-all",
          "geosite:category-ads-ir"'''
        	 
        	 if isIran == '2' :
        	 	if polrn_block=='1' :Wow+=''',
          "geosite:category-porn"'''
        	 	Wow+='''
        ],
        "outboundTag": "block",
        "type": "field"
      },
      {
        "network": "tcp,udp",
        "outboundTag": "warp-out",
        "type": "field"
      },
      {
        "network": "tcp,udp",
        "outboundTag": "warp",
        "type": "field"
      }
    ]
  },
  "stats": {}
}'''

        	 print(Wow), exit()
        
        else: os.system('clear'),print(f'''
{
  {
    "route": {
      {
        "geoip": {
          {
            "path": "geo-assets\\\\sagernet-sing-geoip-geoip.db"
          }
        },
        "geosite": {
          {
            "path": "geo-assets\\\\sagernet-sing-geosite-geosite.db"
          }
        },
        "rules": [
          {
            {
              "inbound": "dns-in",
              "outbound": "dns-out"
            }
          },
          {
            {
              "port": 53,
              "outbound": "dns-out"
            }
          },
          {
            {
              "clash_mode": "Direct",
              "outbound": "direct"
            }
          },
          {
            {
              "clash_mode": "Global",
              "outbound": "select"
            }
          }
        ],
        "auto_detect_interface": true,
        "override_android_vpn": true
      }
    },
    "outbounds": [
      {
        {
          "type": "selector",
          "tag": "select",
          "outbounds": [
            "auto",
            "Ir->ÐΛɌ₭ᑎΞ𐒡𐒡",
            "De->ÐΛɌ₭ᑎΞ𐒡𐒡"
          ],
          "default": "auto"
        }
      },
      {
        {
          "type": "urltest",
          "tag": "auto",
          "outbounds": [
            "Ir->ÐΛɌ₭ᑎΞ𐒡𐒡",
            "De->ÐΛɌ₭ᑎΞ𐒡𐒡"
          ],
          "url": "http://cp.cloudflare.com/",
          "interval": "10m0s"
        }
      },
      {
        {
          "type": "wireguard",
          "tag": "Ir->ÐΛɌ₭ᑎΞ𐒡𐒡",
          "local_address": [
            "172.16.0.2/32",
            "{all_key[0]}"
          ],
          "private_key": "{all_key[1]}",
          "server": "{best_result[0]}",
          "server_port": {best_result[
              1
            ]
          },
          "peer_public_key": "{all_key[3]}",
          "reserved": {all_key[
              2
            ]
          },
          "mtu": 1280,
          "fake_packets": "5-10"
        }
      },
      {
        {
          "type": "wireguard",
          "tag": "De->ÐΛɌ₭ᑎΞ𐒡𐒡",
          "detour": "Ir->ÐΛɌ₭ᑎΞ𐒡𐒡",
          "local_address": [
            "172.16.0.2/32",
            "{all_key2[0]}"
          ],
          "private_key": "{all_key2[1]}",
          "server": "{best_result[0]}",
          "server_port": {best_result[
              1
            ]
          },
          "peer_public_key": "{all_key[3]}",
          "reserved": {all_key2[
              2
            ]
          },
          "mtu": 1280,
          "fake_packets": "5-10"
        }
      },
      {
        {
          "type": "dns",
          "tag": "dns-out"
        }
      },
      {
        {
          "type": "direct",
          "tag": "direct"
        }
      },
      {
        {
          "type": "direct",
          "tag": "bypass"
        }
      },
      {
        {
          "type": "block",
          "tag": "block"
        }
      }
    ]
  }
}
''')	
        if what=="3":
            exit()
                

    
    
    if what=="3":
        main2_1()
        exit()
    


    best_result=main()
    
    if what=='8':
    	
    	rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
    	for n in range(how_many):
    		main2_2()
    	os.system('clear')
    	
    	#upload_to_bashupload
    	upload_to_bashupload(f'''[
  {WoW_v2
  }
]''')
    	exit()
    	
    
    main2_1()

    
def main3():
    global best_result
    global wire_config_temp
    global wire_c
    global wire_p
    if wire_p==0:

         try:
             best_result=main()
         except Exception:
             print("\033[91m")
             print('Try again and choose wire guard without ip')
             print('\033[
  0m')
             exit()
    print(f"please wait make wireguard : {wire_c}. ")
    
    try:
        all_key2=free_cloudflare_account()
    except Exception as E:
            print(' Try again Error =', E)
            exit()
    
    print('\033[
    0m')

    os.system('clear')

    
    try:
        all_key=free_cloudflare_account()
    except Exception as E:
            print(' Try again Error =', E)
            exit()
            
    if wire_p !=1:
    	wire_config_or = f'''

    {
      {
        "type": "wireguard",
        "tag": "𓄂𓆃-IR{wire_c}",
        "server": "{best_result[0]}",
        "server_port": {best_result[
            1
          ]
        },
        "local_address": [
          "172.16.0.2/32",
          "{all_key[0]}"
        ],
        "private_key": "{all_key[1]}",
        "peer_public_key": "{all_key[3]}",
        "reserved": {all_key[
            2
          ]
        },
        "mtu": 1280,
        "fake_packets": "5-10"
      }
    },
    {
      {
        "type": "wireguard",
        "tag": "ÐΛɌ₭ᑎΞ𐒡𐒡-WoW{wire_c}",
        "detour": "𓄂𓆃-IR{wire_c}",
        "server": "{best_result[0]}",
        "server_port": {best_result[
            1
          ]
        },
        "local_address": [
          "172.16.0.2/32",
          "{all_key2[0]}"
        ],
        "private_key": "{all_key2[1]}",
        "peer_public_key": "{all_key2[3]}",
        "reserved": {all_key2[
            2
          ]
        },
        "mtu": 1120
      }
    }

'''
    else:
        wire_config_or = f'''

    ,
    {
      {
        "type": "wireguard",
        "tag": "𓄂𓆃-IR{wire_c}",
        "server": "{best_result[0]}",
        "server_port": {best_result[
            1
          ]
        },
        "local_address": [
          "172.16.0.2/32",
          "{all_key[0]}"
        ],
        "private_key": "{all_key[1]}",
        "peer_public_key": "{all_key[3]}",
        "reserved": {all_key[
            2
          ]
        },
        "mtu": 1280,
        "fake_packets": "5-10"
      }
    },
    {
      {
        "type": "wireguard",
        "tag": "Darkness-Main{wire_c}",
        "detour": "𓄂𓆃-IR{wire_c}",
        "server": "{best_result[0]}",
        "server_port": {best_result[
            1
          ]
        },
        "local_address": [
          "172.16.0.2/32",
          "{all_key2[0]}"
        ],
        "private_key": "{all_key2[1]}",
        "peer_public_key": "{all_key2[3]}",
        "reserved": {all_key2[
            2
          ]
        },
        "mtu": 1120
      }
    }

'''

    if i == int(how_many)-1:
        upload_to_bashupload(f'''{
      {
        "outbounds": [
          {wire_config_temp
          }
        ]
      }
    }
''')
    else:
                    
        wire_config_temp=wire_config_temp+wire_config_or
            
            
    wire_c=wire_c+1
    wire_p=1
def generate_wireguard_url(config, endpoint):
    
    
    required_keys = ['PrivateKey', 'PublicKey' ,'Address'
    ]
    if not all(key in config and config[key
    ] is not None for key in required_keys):
        print("Incomplete configuration. Missing one of the required keys or value is None.")
        return None

    encoded_addresses = [quote(address1) for address1 in (config['Address'
      ])
    ]
    
    address= ','.join(encoded_addresses)
    
    wireguard_urll = (
        f"wireguard://{urlencode(config['PrivateKey'])}@{endpoint}"
        f"?address={address}&"
        f"publickey={urlencode(config['PublicKey'])}"
    )
    
    
    if config.get('Reserved'):
        wireguard_urll += f"&reserved={urlencode(config['Reserved'])}"
    
    wireguard_urll += "#Tel=@darkness_427"

    return wireguard_urll
def start_menu():
    check_ipv=check_ipv6()
    rprint(f'ipv4 : [bold red
    ]{check_ipv[
        0
      ]
    }[/bold red
    ]\nipv6 : [bold red
    ]{check_ipv[
        1
      ]
    }[/bold red
    ]\n')
    
    options = {
      "1": "scan ip",
      "2": "wireguard config",
      "3": "wireguard config without ip scanning",
      "4": "wireguard with a sub link",
      "5": "wireguard for v2ray and mahsaNG",
      "6": "wireguard for v2ray and mahsaNG without ip scanning",
      "7": "WoW for v2ray or mahsaNG",
      "8": "WoW for v2ray or mahsaNG in sub link",
      "9": "Add/Delete shortcut",
      "10": "get wireguard.conf",
      "00": "info",
      "0": "Exit"
    }

    rprint("[bold red]ÐΛɌ₭ᑎΞ𐒡𐒡 𓄂𓆃[/bold red]")
    for key, value in options.items():
        rprint(f" [bold yellow]{key}[/bold yellow]: {value}")
    what = Prompt.ask("Choose an option", choices=list(options.keys()), default="0")
    return what
def get_number_of_configs():
    while True:
        try:
            how_many = int(Prompt.ask('\nHow many configs do you need (2 to 15): '))
            if how_many >= 2 and how_many <= 15:
                break
        except ValueError:
            console.print("[bold red]Please enter a valid number![/bold red]", style="red")
    return how_many
def gojo_goodbye_animation():
    frames  = [
        "\n\033[94m(＾-＾)ノ\033[0m",  # آبی
        "\n\033[93m(＾-＾)ノ~~~\033[0m",  # زرد
        "\n\033[92m(＾-＾)ノ~~~~~~\033[0m", # سبزl
    ]
    
    for frame in frames:
      #  os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(1)
if __name__ == "__main__":
    os.system('clear')
    
    what=start_menu()


    if what =='1':
        
        do_you_save=input_p('Do you want to save in a result csv\n',
    {
      "1": 'Yes' ,
      "2": "No"
    })
        which = 'n'
        if do_you_save=='1':
        	os.system('termux-setup-storage')
        	which = input_p('Do you want for bpb panel(with comma) or vahid panel(with enter) in a result csv\n ',
    {'1' : 'bpb panel(with comma)',
        	 '2' : 'vahid panel(with enter)'
    })
       
            
        main()
    elif what=='2' or what=="3" or what =='7':
    
        if what == '7':
        	
        	polrn_block= input_p('Do you want to block p@rn sites\n' ,
    {
      "1": "Yes",
      "2": "No"
    })
        	
        	isIran =input_p('Iran or Germany\n' ,
    {
      "1": "Ip Iran[faster speed]",
      "2": "Germany[slower speed]"
    })
        	
        	
        main2()
    elif what=='4':
        how_many=get_number_of_configs()  

        for i in range(how_many):
            main3()
    elif what =='5' or what =='6':
        
        	
        api_url = 'https: //api.zeroteam.top/warp?format=sing-box'
        if what=='5':
        	endpoint_ip_best_result=main()
        	endpoint_ip = str(endpoint_ip_best_result[
      0
    ])+":"+str(endpoint_ip_best_result[
      1
    ])
        else:
            endpoint_ip=input('Enter ip with port (defualt = n):')
            if endpoint_ip=='N' or  endpoint_ip=='n':
                endpoint_ip="162.159.195.166:878"
            else:
                temp_ip2=''
                temp_port2=''
                temp_c2=0
                while endpoint_ip[temp_c2
    ] !=':':
                        temp_ip2=temp_ip2+endpoint_ip[temp_c2
    ]
                        temp_c2=temp_c2+1
                            
                        
                set_enter_ip2=endpoint_ip.index(":")
                temp_port2=endpoint_ip[set_enter_ip2+1:
    ]
                    

                    
                    
                    #temp_port=temp_port+enter_ip[i
    ]
                endpoint_ip=[temp_ip2, int(temp_port2)
    ]
                
                
        rprint("[bold green]Please wait, generating WireGuard URL...[/bold green]")
        try:
            config = fetch_config_from_api()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        wireguard_url = generate_wireguard_url(config, endpoint_ip)
        if wireguard_url:
            os.system('clear')
            print(f"""{wireguard_url
    }




""")
        else:
            print("Failed to generate WireGuard URL.")
    elif what == '8':
    	how_many=get_number_of_configs()
    	polrn_block= input_p('Do you want to block p@rn sites\n' ,
    {
      "1": "Yes",
      "2": "No"
    })

    	
    	main2()
    
    elif what == '9':

    	if os.path.exists('/data/data/com.termux/files/usr/etc/bash.bashrc.bak'):
    		
    		Delete=input_p('Do you want to Delete short cut',
    {
      "1": "Yes",
      "2": "No"
    })
    		if Delete=='1':
    			os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
    			os.rename('/data/data/com.termux/files/usr/etc/bash.bashrc.bak', '/data/data/com.termux/files/usr/etc/bash.bashrc')
    			console.print("[bold red]Shortcut Deleted,  successful[/bold red]", style="red")
    
    
    		exit()
    	while True:
    		name = input("\nEnter a shortcut name : ")
    		if not name.isdigit():
    			break
    			
    		
    		else:
    			console.print("\n[bold red]Please enter a name![/bold red]", style="red")
    			
    	with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r') as f2:
    		txt= f2.read()
    		with open('/data/data/com.termux/files/usr/etc/bash.bashrc.bak', 'w') as f:
    			f.write(txt)
    	text=f'''
{name
    }() {
      {
bash <(curl -fsSL https: //raw.githubusercontent.com/darknessm427/WarpScanner/main/install.sh)
      }
    }\n'''
    	with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r+') as f:
    	   	content = f.read()
    	   	f.seek(0,
    0)
    	   	f.write(text.rstrip('\r\n') + '\n' + content)
    	rprint(f"\n[bold green]Please Restart your  termux and Enter [bold red]{name}[/bold red] to run script[/bold green]")

    elif what =='10':
        endpoint_ip_best_result=main()
        endpoint_ip = str(endpoint_ip_best_result[
      0
    ])+":"+str(endpoint_ip_best_result[
      1
    ])
        try:
            all_key=free_cloudflare_account()
        except Exception as E:
            print(' Try again Error =', E)
            exit()
        name_conf=input('\nEnter a name: (defult [Enter
    ]) : ')
        
        os.system('termux-setup-storage')
        
        	
        
        if name_conf=='' :
        	
        	name_conf='ACPwire.conf'
        path = '/storage/emulated/0/'+name_conf
        with open(path, 'w') as f:
        	f.write(f'''[Interface
    ]
PrivateKey = {all_key[
        1
      ]
    }
Address = 172.16.0.2/32,
    {all_key[
        0
      ]
    }
DNS = 1.1.1.1,
    1.0.0.1,
    2606: 4700: 4700: : 1111,
    2606: 4700: 4700: : 1001
MTU = 1280

[Peer
    ]
PublicKey = {all_key[
        3
      ]
    }
AllowedIPs = 0.0.0.0/0,
    : :/0
Endpoint = {endpoint_ip
    }''')
        rprint(f'\n[bold green
    ]{name_conf
    } saved in {path
    }.conf[/bold green
    ]')
    
    elif what == '00':
    	info()
    	
    elif what=='0':
        gojo_goodbye_animation()
        time.sleep(1)
        console.print("""[bold magenta
    ]Exiting... Goodbye![/bold magenta
    ]""")
        
        
        exit()
