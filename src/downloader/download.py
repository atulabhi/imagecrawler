import sys
import requests
sys.path.append("..")
from imgstore.store import LocalStore

class Downloader:
    # parameterized constructor
    def __init__(self,store):
        self.store = store
    # Donwload method to download image from url
    def Save(self,assets):
        count = 0
        print("Total {len(assets)} Image Found!")
        for i, imageUrl in enumerate(assets):
            print("downloading image for ", imageUrl)
            imageContent = requests.get(imageUrl).content
            self.store.save(imageContent, "img-"+str(count))
            count=count+1
        if count == len(assets):
            print("All Images Downloaded!")
            print (count)
        else:
            print(f"Total {count} Images Downloaded Out of {len(assets)}")

 