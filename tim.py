from bs4 import BeautifulSoup   
import requests

url = "https://www.16thcircuit.org/courtapps/dlt/browseall.asp?index=0"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")

tbody = doc.body
trs = tbody.contents
content= doc.find_all(class_='datafield')
label = doc.find_all(class_='labels')

for tr in content:
   
    #print(name)
    print(tr.fi)
    #print(",")
    #print(label)
