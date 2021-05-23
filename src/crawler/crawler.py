import requests
import time
from bs4 import BeautifulSoup
from queue import Queue
import os 
assets = []
links = []
url = 'https://www.geeksforgeeks.org/'
tmpStore = '/home/atul/Desktop/testimage/'
allowedDepth = 1

class URL:
  def __init__(self, url, depthLevel):
    self.url = url
    self.depthLevel = depthLevel

def fetch(url):
    assetTracker = {}
    linkTracker = {}
    print("inside fetch function")
    depthLevel = 0
    urlQueue = Queue()
    gotUrl = URL(url,0)
    urlQueue.put(gotUrl)
    linkTracker[url]="true"
    while  not urlQueue.empty():
        imageUrl = urlQueue.get()
        actualUrl = imageUrl.url
        depthLevel = imageUrl.depthLevel
        #print("fetching page for url", actualUrl)
        getPage = requests.get(actualUrl)
        pageContent = BeautifulSoup(getPage.text,"html.parser")
        imageLinks = pageContent.find_all('img')
        print("queue is empty",urlQueue.empty())
        print("fetched url",actualUrl)
        for imageUrl in imageLinks:
            gotImageURL=imageUrl.get('src')
            if gotImageURL and  "http" in gotImageURL: 
                if not gotImageURL in assetTracker:
                    assetTracker[gotImageURL]="true"
                    assets.append(gotImageURL)   
        if depthLevel <= allowedDepth:
            newLinks = pageContent.find_all('a')
            for linkUrl in newLinks:
                gotLinkURL=linkUrl.get('href')
                if gotLinkURL and  "http" in gotLinkURL:
                    if not gotLinkURL in linkTracker:
                        linkTracker[gotLinkURL]="true"
                        links.append(gotLinkURL)
                        if not depthLevel >= allowedDepth:
                            gotUrl = URL(gotLinkURL,depthLevel=+1)
                            urlQueue.put(gotUrl)
    return assets, links

def getWebsiteAssets(url):
    assets,links = fetch(url)
    downloadImage(assets, tmpStore)

#    print("*----------------------Assets--------------------------------------------------*")
#    print(len(assets))
#    print("*----------------------Links--------------------------------------------------*")
#    print(len(links))


def downloadImage(assets, tmpStore):
    count = 0
    print(f"Total {len(assets)} Image Found!")
    for i, imageUrl in enumerate(assets):
       imageContent = requests.get(imageUrl).content
       with open(f"{tmpStore}/images{i+1}.jpg", "wb+") as f:
                        f.write(imageContent)
                        count += 1
    if count == len(assets):
            print("All Images Downloaded!")
            print (count)
        # if all images not download
    else:
       print(f"Total {count} Images Downloaded Out of {len(assets)}")
    

getWebsiteAssets(url)
