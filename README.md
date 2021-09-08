## Masscan Organizer
This script will accept a masscan xml result file, and output lists of ips, grouped by open ports

For example:

`sudo masscan -p 10,20 0.0.0.0/8 -oX out.xml`

### Prerequisites
- python 3
- python 3 lxml parser `apt install python3-lxml`
- beautifulSoup module `pip install bs4`
(bs4 docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc)

### Usage
`python3 masscan_organizer.py masscan_file.xml`
Output files will be created in the working directory; one for each unique open port in your file (so like, this could be many!!)
_for example, mso\_80.txt, mso\_443.txt, mso\_22.txt: each of these will contain a list of hosts which have this port open_

### Enjoy, and hack the planet and stuff <3

### Using pipenv

```bash
pipenv run pip install -r requirements.txt
pipenv run python masscan_organizer.py out.xml
```
