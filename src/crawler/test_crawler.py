import unittest
from crawler.crawler import *
from fetcher.requests import *
from store.store import *

class TestTracker(unittest.TestCase):
    def test_visited_1(self):
        tracker=Tracker()
        imagelink="https://dummy.dev.io"
        tracker.addImageLink(imagelink)
        assert bool(tracker.isImageLinkVisited(imagelink)) == True
        assert bool(tracker.isWebLinkVisited(imagelink)) == False
    def test_visited_2(self):
        tracker=Tracker()
        weblink="https://dummy.dev.io"
        tracker.addWebLink(weblink)
        assert bool(tracker.isImageLinkVisited(weblink)) == False
        assert bool(tracker.isWebLinkVisited(weblink)) == True
    def test_visited_3(self):
        tracker=Tracker()
        assert bool(tracker.isImageLinkVisited("https://www.google.com")) == False
        assert bool(tracker.isWebLinkVisited("https://www.flipkart.com")) == False


class TestURLDescriptor(unittest.TestCase):
    def test_ud_1(self):
        url="https://dummy1.dev.io"
        ud=UrlDescriptor(url,3)
        self.assertEqual(ud.getURL(),url)
        self.assertEqual(ud.getDepthLevel(),3)
    def test_ud_2(self):
        url="https://dummy2.dev.io"
        ud=UrlDescriptor(url,0)
        self.assertEqual(ud.getURL(),url)
        self.assertEqual(ud.getDepthLevel(),0)
    def test_ud_3(self):
        url="https://dummy3.dev.io"
        ud=UrlDescriptor(url,1)
        self.assertEqual(ud.getURL(),url)
        self.assertEqual(ud.getDepthLevel(),1)

class TestGetWebsiteAssets(unittest.TestCase):
    def test_getassets1(self):
        url="https://www.geeksforgeeks.org/"
        req=FakeRequest()
        new_store=MockStore()
        f=Fetcher(0,req,new_store)
        totalAssets,totalLinks=f.GetWebsiteAssets(url)
        print("totalassets: ",totalAssets)
        print("totallinks: ",totalLinks)
        self.assertEqual(totalAssets,8)
        self.assertEqual(totalLinks,237)
    def test_getassets2(self):
        url="https://www.geeksforgeeks.org/"
        req=FakeRequest()
        new_store=MockStore()
        f=Fetcher(1,req,new_store)
        totalAssets,totalLinks=f.GetWebsiteAssets(url)
        self.assertEqual(totalAssets,8)
        self.assertEqual(totalLinks,237)
    def test_getassets3(self):
        url="https://openebs.io/"
        req=FakeRequest()
        new_store=MockStore()
        f=Fetcher(1,req,new_store)
        totalAssets,totalLinks=f.GetWebsiteAssets(url)
        self.assertEqual(totalAssets,6)
        self.assertEqual(totalLinks,13)


