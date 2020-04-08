import requests
from bs4 import BeautifulSoup

search =input("Search for:")
params ={"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text,"html.parser")
result= soup.find("ol", {"id": "b_results"})
link = result.findAll("li", {"class":"b_algo"})

for item in link:
    item_text =item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
     print (item_text)
     print (item_href)
     print("parent",item.find("a").parent)



