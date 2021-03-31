import requests
from bs4 import BeautifulSoup

req = requests.get("https://csie.asia.edu.tw/project/semester-103"
)
req.encoding = "big5"

if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result = soup.find_all("li")                 #注意網頁內容標籤
    fp = open("out2.txt","w",encoding="utf8")
    for val in result:
        text2 = val.text.replace("\n", " ")
        text3 = text2.replace("  " , " ")
        print(text3)
        fp.write(text3+"\n")
    fp.close()
    print(result)
else:
    print("no page")