from downloader.download import Downloader
from store.store import LocalStore
from bs4 import BeautifulSoup
from queue import Queue
import os 

# UrlDescriptor holds the url link and its depth level
class UrlDescriptor:
    def __init__(self, url, depthLevel):
        self.url = url
        self.depthLevel = depthLevel
    def getURL(self):
        return self.url
    def getDepthLevel(self):
        return self.depthLevel

# Tracker tracks the visited <a> weblinks and (<img>) imagelinks
class Tracker:
    def __init__(self):
        self.imageTracker = {}
        self.linkTracker = {}
    # addImageLink  marks the provided imagelink as visited/processed
    def addImageLink(self,link):
        self.imageTracker[link]="true"
    # addWebLink marks the provided weblink visited/processed
    def addWebLink(self,link):
        self.linkTracker[link]="true"
    # isWebLinkVisited returns true if the weblink is already visited/processed for 
    # crawling its further child links
    def isWebLinkVisited(self,link):
        if link in self.linkTracker:
            return True
    # isImageLinkVisited returns true if the image link is already visited/processed for 
    # download
    def isImageLinkVisited(self,link):
        if link in self.imageTracker:
            return True

class Fetcher:
    def __init__(self,allowedDepth,requests,store):
        self.tracker = Tracker()
        self.queue = Queue()
        self.allowedDepth=allowedDepth
        self.requests = requests
        self.store=store
        self.assets = []
        self.links = []

    def GetWebsiteAssets(self,url):
        self.Fetch(url)
        d=Downloader(self.store,self.requests)
        d.Save(self.assets)
        return len(self.assets), len(self.links)

    def Fetch(self,url):
        print("fetching from the base url: ",url)
        ud=UrlDescriptor(url,0)
        self.queue.put(ud)
        self.tracker.addWebLink(url)
        while not self.queue.empty():
            ud = self.queue.get()
            url = ud.getURL()
            print("Processing url: ",url)
            currentDepth = ud.getDepthLevel()
            pageContent=self.getPageContent(url)
            gotImageLinks=self.getImageLinks(pageContent)
            gotWebLinks=self.getWebLinks(pageContent, currentDepth)

    def getPageContent(self,url):
        # This is the bottle neck 
        getPage = self.requests.get(url)
        pageContent = BeautifulSoup(getPage.text,"html.parser")
        return pageContent

    def getImageLinks(self,pageContent):
        imageLinks = pageContent.find_all('img')
        for imageUrl in imageLinks:
            gotImageURL=imageUrl.get('src')
            if gotImageURL and  "http" in gotImageURL: 
                if not self.tracker.isImageLinkVisited(gotImageURL):
                    self.tracker.addImageLink(gotImageURL)
                    self.assets.append(gotImageURL) 
        
    def getWebLinks(self,pageContent,currentDepth):
        newLinks = pageContent.find_all('a')
        for linkUrl in newLinks:
            gotLinkURL=linkUrl.get('href')
            if gotLinkURL and  "http" in gotLinkURL:
                if not self.tracker.isWebLinkVisited(gotLinkURL):
                    self.tracker.addWebLink(gotLinkURL)
                    self.links.append(gotLinkURL)
                    if not currentDepth >= self.allowedDepth:
                        gotUD=UrlDescriptor(gotLinkURL,currentDepth+1)
                        self.queue.put(gotUD)

    






