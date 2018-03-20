# -*-coding:utf-8-*-  
from scrapy.spiders import Spider
from scrapy import Request
from bs4 import BeautifulSoup
from fjSpider.items.anjuke_items import anjukeItem
from urllib.parse import urljoin

class anjukeSpider(Spider):
    name='anjuke-GFsundeXQ'
    url = 'https://foshan.anjuke.com/community/shundequ/o6-p%d/'
    custom_setting={

    }

    def start_requests(self):
        for i in range(50):
            yield Request(url%(i+1),callback=self.parse)

    def parse(self,response):
        soup=BeautifulSoup(response.body,'lxml',from_encoding='utf-8')
        divs=soup.find_all('div',class_='li-itemmod')
        for div in divs:
            link=urljoin(response.url,div['link'])
            yield Request(link,callback=self.second_parse)

    def second_parse(self,response):
        url
        
