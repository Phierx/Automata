import requests 
from bs4 import BeautifulSoup

#req = requests.get("https://www.16thcircuit.org/browse-all-parcels")
req = requests.get("https://www.16thcircuit.org/courtapps/dlt/browseall.asp?index=0")

soup = BeautifulSoup(req.content,"html.parser")


#res = soup.body.
job_title = soup.find_all(class_='datafield')

for job in job_title:
    print(job.text)
    