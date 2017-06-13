# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class TutorialPipeline(object):

    CSV_FILENAME = 'C:\\Users\\shadow_xu\\Desktop\\New Text Document.txt'

    def process_item(self, item, spider):
        line = item['address'] + '  ' + item['title'] + '  ' + item['body'] + os.linesep
        with open(self.CSV_FILENAME, 'a+') as fp:
            fp.write(line.encode('utf8'))
        return item
