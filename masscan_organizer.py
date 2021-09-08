import sys
from bs4 import BeautifulSoup

# This script will accept a masscan xml result file, and output lists of ips, grouped by open ports
# for example, mso_80.txt, mso_443.txt, mso_22.txt
# this requires an lxml parser and the beautifulSoup module
# apt install python3-lxml
# helps https://www.crummy.com/software/BeautifulSoup/bs4/doc

# Arg 1 is masscan xml output file
scan = sys.argv[1]

with open(scan) as f:
    soup = BeautifulSoup(f, "lxml")
  
hosts = soup.find_all('address')
for i in range(0, len(hosts)):
    host = hosts[i]
    ip = host['addr']
    sib = host.find_next_sibling('ports')
    port = sib.findChildren("port")[0]['portid']
    outfile = f"mso_{port}.txt"
    with open (outfile, "a+") as f:
        f.seek(0)
        if ip not in f.read():
            f.write(f"{ip}\n")