import unittest
from download import Downloader
class TestDonwloader(unittest.TestCase):
    def test_download(self):
        d=Downloader("imageurl","localstore")
        d.Download()
if __name__ == '__main__':
    unittest.main()
