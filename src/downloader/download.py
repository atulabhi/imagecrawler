import sys
from store.store import LocalStore

class Downloader:
    # parameterized constructor
    def __init__(self,store,requests):
        self.store = store
        self.requests = requests
    # Donwload method to download image from url
    def Save(self,assets):
        count = 0
        for i, imageUrl in enumerate(assets):
            try:
                imageContent = self.requests.get(imageUrl).content
                if self.store.save(imageContent, "img-"+str(count)):
                    count=count+1
            except IOError:
                print("failed to download image content from url ",imageUrl)
                continue
        return count

 