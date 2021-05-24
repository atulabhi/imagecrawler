import sys
sys.path.append("..")
from downloader.download import Downloader
from imgstore.store import LocalStore
import requests
import time
from bs4 import BeautifulSoup
from queue import Queue
import os 
assets = []
links = []
url = 'https://www.geeksforgeeks.org/'
allowedDepth = 0

# UrlDescriptor holds the url link and its depth level
class UrlDescriptor:
    def __init__(self, url, depthLevel):
        self.url = url
        self.depthLevel = depthLevel
    def getURL(self):
        return self.url
    def getDepthLevel(self):
        return self.depthLevel

# Tracker tracks the visited <a> links and image (<img>) links
class Tracker:
    imageTracker = {}
    linkTracker = {}
    def addImageLink(self,link):
        self.imageTracker[link]="true"
    def addWebLink(self,link):
        self.linkTracker[link]="true"
    def isWebLinkVisited(self,link):
        if link in self.linkTracker:
            return True
    def isImageLinkVisited(self,link):
        if link in self.imageTracker:
            return True



def fetch(url):
    tracker=Tracker()
    print("inside fetch function")
    urlQueue = Queue()
    ud=UrlDescriptor(url,0)
    urlQueue.put(ud)
    tracker.addWebLink(url)
    while  not urlQueue.empty():
        ud = urlQueue.get()
        actualUrl = ud.getURL()
        depthLevel = ud.getDepthLevel()
        print("fetching page for url", actualUrl)
        getPage = requests.get(actualUrl)
        pageContent = BeautifulSoup(getPage.text,"html.parser")
        imageLinks = pageContent.find_all('img')
        print("queue is empty",urlQueue.empty())
        print("fetched url",actualUrl)
        for imageUrl in imageLinks:
            gotImageURL=imageUrl.get('src')
            if gotImageURL and  "http" in gotImageURL: 
                if not tracker.isImageLinkVisited(gotImageURL):
                    tracker.addImageLink(gotImageURL)
                    assets.append(gotImageURL)   
        if depthLevel <= allowedDepth:
            newLinks = pageContent.find_all('a')
            for linkUrl in newLinks:
                gotLinkURL=linkUrl.get('href')
                if gotLinkURL and  "http" in gotLinkURL:
                    if not tracker.isWebLinkVisited(gotLinkURL):
                        tracker.addWebLink(gotLinkURL)
                        links.append(gotLinkURL)
                        if not depthLevel >= allowedDepth:
                            gotUD=UrlDescriptor(gotLinkURL,depthLevel+1)
                            urlQueue.put(gotUD)
    return assets, links

def getWebsiteAssets(url):
    assets,links = fetch(url)
    store=LocalStore()
    d=Downloader(store)
    d.Save(assets)
    #downloadImage(assets, tmpStore)


getWebsiteAssets(url)



