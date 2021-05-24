import unittest
from crawler import *

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



if __name__ == '__main__':
    unittest.main()