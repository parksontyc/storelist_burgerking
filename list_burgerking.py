import requests
from bs4 import BeautifulSoup
import time
import csv

store_name = []
store_address = []

for i in range(0, 6):

	url = "https://www.burgerking.com.tw/store.php?p="+str(i)+"&c=0&t=0"

	res = requests.get(url, timeout=2)

	html = res.text

	soup = BeautifulSoup(html.replace("\n", "").strip(), "html.parser")

	items = soup.find_all("ul", class_="store_info")

	for item in items:
		name = item.li
		name = name.text
		store_name.append(name[5:])
		address = item.find("a", target="_blank")
		store_address.append(address.text)
		print(store_name, store_address)

with open('shop_list_burgerking.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        csvwriter.writerow(newrow)
        
#for item in items:
	#address = item.find("a", target="_blank")
	#store_address.append(address.text)
	#print(store_address)


