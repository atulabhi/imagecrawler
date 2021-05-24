## imagecrawler


A web crawler to crawl a website and download the images.


#### USAGE (bash):
```bash
python3 crawler.py test.py 
```
#### Design Notes

+ All links are stored in assests and link variable.

+ A queue is used to store the new links found on the page with depthlevel.

+ Downloader module is used to download the images.

+ Store  module is used to specify the location where  the images will be stored for now only local is supported 

+ Images are getting stored in /tmp/images directory so images dir should be present in /tmp.   

+ AllowedRun level should be used to specify the depth level wanted to crawl.



####  Test:

There is a unit test coverege:

```bash
python3 test_crawler.py
```
