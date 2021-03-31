import requests
from bs4 import BeautifulSoup

req = requests.get("https://csie.asia.edu.tw/project/semester-103"
)
req.encoding = "utf-8"       #注意編碼


soup = BeautifulSoup(req.text, "lxml")               #注意網頁內容標籤
fp = open("out1.txt","w",encoding="utf8")
for table in soup.find_all("table"):

    for row in table.find_all("tr"):
            
        for result in row.find_all("td"):

            result = result.text.replace(" \t," "").replace("\n","")
            fp.write(result + "\t")
            
        fp.write("\n")

    fp.write("\n")

fp.close()
print(result)