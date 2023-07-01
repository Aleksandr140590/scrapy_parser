import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps_links = response.css("a[href^='pep-']")
        for pep_link in all_peps_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r'PEP (?P<number>\d+) – (?P<name>.*)'
        pep_title_text = response.css('h1.page-title::text').get().strip()
        text_match = re.search(pattern, pep_title_text)
        if text_match is not None:
            number, name = text_match.groups()
        else:
            # на pep 499 название собрано из частей
            number = re.search(r'PEP (?P<number>\d+)', pep_title_text).groups()
            name = pep_title_text
        data = {
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get()
        }
        return PepParseItem(data)
