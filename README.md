## imagecrawler


A web crawler to crawl a website and download the images.


#### USAGE (bash):
+ Clone the repo 

+ CD inside src

+ Install required modules using pip from requrement.txt

+ Run below command
```bash
python3 main.py
```
+ You will be asked to provide the url to crawl and the depth level till which you want the crawling to happen

+ Sample Input : In this input, we want to crawl https://openebs.io at a depth level of 0 meaning only the first page assets will be 
saved and the subsequent next links will not be fetched to get the assets.
```
Enter url to crawl
https://openebs.io
Enter depth level to crawl
0
```
#### Design Notes

+ All links are stored in assests and link instance variable of Fetch class.

+ To crawl the website, BFS has been used and the depth of crawling can be controlled.

+ Downloader module is used to download the images.

+ Store  module is used to specify the location where  the images will be stored for now only local is supported 



####  Test:

There is a unit test coverege:

```bash
python3 -m unittest crawler/test_crawler.py
```
