import unittest
from downloader.download import Downloader
from store.store import *
from fetcher.requests import *

class TestDonwloader(unittest.TestCase):
    def test_download_1(self):
        assets=["dummylink1","dummylink2"]
        new_store=MockStore()
        new_req=FakeRequest()
        d=Downloader(new_store, new_req)
        self.assertEqual(d.Save(assets),len(assets))
    def test_download_2(self):
        assets=["dummylink1","dummylink1","dummlin6"]
        new_store=MockStore()
        new_req=FakeRequest()
        d=Downloader(new_store, new_req)
        self.assertEqual(d.Save(assets),len(assets))
