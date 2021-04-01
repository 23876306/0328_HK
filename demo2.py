import requests
from bs4 import BeautifulSoup

req = requests.get("https://csie.asia.edu.tw/project/semester-103"
)
req.encoding = "utf8"

soup = BeautifulSoup(req.text, "lxml")       
fp = open("out2.txt","w",encoding="utf8")

if req.status_code == 200:
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            for cell in row.find_all("td"):
                result = result.text.replace("\t","").replace("\n","")
                fp.write(result + "\n")
            fp.write("/n")
        fp.write("\n")
    fp.close()
else:
    print("no found")