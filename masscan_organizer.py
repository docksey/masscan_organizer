#!/usr/bin/env python
import sys
from bs4 import BeautifulSoup

SCAN = sys.argv[1]

def main():
    with open(SCAN) as f:
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

if __name__ == "__main__":
    main()


