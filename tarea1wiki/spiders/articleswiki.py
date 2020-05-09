# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.markup import remove_tags
from tarea1wiki.items import articleswiki,article

class ArticleswikiSpider(scrapy.Spider):
    name = 'articleswiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': 25,
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'file:C://Data//featured_article-%(time)s.json'
    }

    
    def parse(self, response):
        host = self.allowed_domains[0]
        n = 0
        for link in response.css(".featured_article_metadata > a"):
            url = f"https://{host}{link.attrib.get('href')}"
            yield response.follow(url, callback=self.parse_article, meta = {'link': url})
            
    def parse_article(self, response):
        articulos = articleswiki()
        articulo = article()
        articulos["link"] = response.meta["link"]
        articulo['title'] = remove_tags(response.css("#firstHeading").extract()[0])
        for p in response.css(".mw-parser-output > p").extract():
            paragraph = remove_tags(p)
            if not paragraph.isspace():
                articulo['paragraph'] = paragraph
                break
        articulos["body"] = articulo
        return articulos
