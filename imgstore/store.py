from abc import ABC, abstractmethod
  
class Store(ABC):
    @abstractmethod
    def save(self):
        pass
  
class LocalStore(Store):
    def save(self,imageContent,imageFileName):
        print("saving image using localstore")
        with open(f"/tmp/images/"+imageFileName+".jpg", "wb+") as f:
            f.write(imageContent)

class Minio(Store):
    def save(self):
        print("could not save image using minio: not implemented")


