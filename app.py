import asyncio
import json
from nmap import PortScannerAsync

async def run_nmap_scan(ip_list, port_list):
    nmap = PortScannerAsync()
    open_ports = {}
    closed_ports = {}

    def callback_result(host, scan_result):
        open_ports[host] = []
        closed_ports[host] = []
        for port in scan_result['scan'][host]['tcp']:
            if scan_result['scan'][host]['tcp'][port]['state'] == 'open':
                open_ports[host].append(port)
            elif port in port_list:
                closed_ports[host].append(port)

    await nmap.scan(hosts=' '.join(ip_list), arguments='-p ' + ','.join(map(str, port_list)), callback=callback_result)

    result = {'open_ports': open_ports, 'closed_ports': closed_ports}
    print(json.dumps(result, indent=4))

if __name__ == '__main__':
    with open('ip_list.txt', 'r') as f:
        ip_list = [line.strip() for line in f.readlines()]
    with open('port_list.txt', 'r') as f:
        port_list = [int(line.strip()) for line in f.readlines()]

    asyncio.run(run_nmap_scan(ip_list, port_list))
