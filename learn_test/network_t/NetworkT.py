from time import time
from threading import Thread
import requests

class DownloadTaskHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao'+filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    dateModel = resp.json()
    for image in dateModel['newlist']:
        url = image['picUrl']
        DownloadTaskHanlder(url).start()

if __name__ == '__main__':
    main()