import requests
from bs4 import BeautifulSoup

req = requests.get("https://csie.asia.edu.tw/project/semester-103"
)
req.encoding = "utf8"

if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result = soup.find_all("table")
    result_2= soup.find_all("tr")
    result_3 = soup.find_all("td")                 #注意網頁內容標籤
    fp = open("out1.txt","w",encoding="utf8")
    for val in result:
        text2 = val.text.replace("\n", " ")
        text3 = text2.replace("  " , " ")
        print(text3)
        fp.write(text3+"\n")
    fp.close()
    for val in result_2:
        text2 = val.text.replace("\n", " ")
        text3 = text2.replace("  " , " ")
        print(text3)
        fp.write(text3+"\n")
    fp.close()
    for val in result_3:
        text2 = val.text.replace("\n", " ")
        text3 = text2.replace("  " , " ")
        print(text3)
        fp.write(text3+"\n")
    fp.close()
else:
    print("no page")

#用課堂練習方法-----錯誤,需更改