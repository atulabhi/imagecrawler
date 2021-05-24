from crawler.crawler import Fetcher
from fetcher.requests import *
from store.store import LocalStore


def main():
    url = input("Enter url to crawl\n")
    allowedDepthLevel = input("Enter depth level to crawl\n")
    req=RequestHTTP()
    new_store=LocalStore()
    f=Fetcher(int(allowedDepthLevel),req,new_store)
    totalAssets,totalLinks=f.GetWebsiteAssets(url)
    print("Total Links = ", totalLinks)
      
if __name__=="__main__":
    main()
