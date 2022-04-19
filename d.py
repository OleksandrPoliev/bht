import os
import requests
import json

class gbooks():
    googleapikey=""

    def search(self, value):
        params = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=params)
        print(r)
        rj = r.json()
        d=rj['items'][1]['volumeInfo']
        print(d)
        title=d['title']
        authors=d['authors'][0]
        publishedDate=d['publishedDate']
        pageCount=d['pageCount']
        language=d['language']
        img=d['imageLinks']['smallThumbnail']
        print(img)
        # isbn=d['industryIdentifiers'][1]['identifier']

        j = rj['items'][1]['volumeInfo']['publishedDate'][:4]




bk = gbooks()
bk.search("horse")