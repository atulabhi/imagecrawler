from abc import ABC, abstractmethod
  
class Store(ABC):
    @abstractmethod
    def save(self,imageContent,imageFileName):
        pass
  
class LocalStore(Store):
    def save(self,imageContent,imageFileName):
        absFilePath="/tmp/images/"+imageFileName+".jpg"
        try:
            with open(absFilePath,"wb+") as f:
                try:
                    f.write(imageContent)
                    print("saving asset: ",imageFileName)
                    return True
                except IOError:
                    print("could not write image content to file: ", imageFileName)
                    return False
        except IOError:
            print("could not open path "+"/tmp/images/"+imageFileName+".jpg to write image content")
            return False


class Minio(Store):
    def save(self,imageContent,imageFileName):
        print("could not save image using minio: not implemented")
        return False

class MockStore(Store):
    def save(self,imageContent,imageFileName):
        return True


