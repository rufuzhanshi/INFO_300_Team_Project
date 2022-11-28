# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Address = scrapy.Field()
    Salary = scrapy.Field()
    Work_Frequency = scrapy.Field()
    Work_Period = scrapy.Field()
    Company_Name = scrapy.Field()
    Company_Employee_Number = scrapy.Field()
    Detail_Url = scrapy.Field()

