import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import BossjobItem
import time
from urllib.parse import urljoin

class JobBoss(scrapy.spiders.Spider):
    name = "JobBoss"
    allowed_domains = ["shixiseng.com"]
    page = 1
    start_urls = ["https://www.shixiseng.com/interns?page=1&type=intern&keyword=%E6%B8%B8%E6%88%8F&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="]



    def parse(self, response):
        def decode_num(self, attr):
            attr = attr.encode("utf-8")
            print(attr)
            attr = attr.replace(b'\xee\x88\xa8', b'0')
            attr = attr.replace(b'\xef\x80\xa7', b'1')
            attr = attr.replace(b'\xef\x88\x9c', b'2')
            attr = attr.replace(b'\xee\x9f\xae', b'3')
            attr = attr.replace(b'\xef\xa3\xac', b'4')
            attr = attr.replace(b'\xef\x98\x83', b'5')
            attr = attr.replace(b'\xef\x94\x84', b'6')
            attr = attr.replace(b'\xee\xaf\xba', b'8')
            attr = attr.replace(b'\xee\x8e\xaa', b'g')
            attr = attr.replace(b'\xee\xbb\xaa', b's')
            attr = attr.replace(b'\xee\xba\x87', b'U')
            attr = attr.replace(b'\xee\x85\x9b', b'D')
            attr = attr.replace(b'\xef\x9b\x86', b'C')
            attr = attr.replace(b'\xee\x99\xaf', b'7')
            attr = attr.replace(b'\xef\x97\x93', b'F')
            attr = attr.replace(b'\xef\x90\x80', b'P')
            attr = attr.replace(b'\xee\xb4\xa0', b'S')
            attr = attr.replace(b'\xee\xba\xa0', b'V')
            attr = attr.replace(b'\xef\x86\xb2', b'B')
            attr = attr.replace(b'\xef\x83\x9f', b'T')
            attr = attr.replace(b'\xee\xaf\x93', b'A')
            attr = attr.replace(b'\xee\xbc\xb7', b'R')
            attr = attr.replace(b'\xee\x8d\xa5', b'G')
            attr = attr.replace(b'\xef\x99\xa2', b'a')
            attr = attr.replace(b'\xee\xa6\xbb', b'm')
            attr = attr.replace(b'\xee\x9d\xad', b'e')
            attr = attr.replace(b'\xef\x99\xa0', b'Q')
            attr = attr.replace(b'\xef\x98\x96', b'I')
            attr = attr.replace(b'\xef\x9c\xbd', b'n')
            attr = attr.replace(b'\xee\x95\x90', b't')
            attr = attr.replace(b'\xee\x9d\xad', b'e')
            attr = attr.replace(b'\xee\xb3\x84', b'r')
            attr = attr.replace(b'\xef\x9c\xbd', b'n')
            attr = attr.replace(b'\xee\x9b\xa7', b'E')
            attr = attr.replace(b'\xef\x89\xaf', b'u')
            attr = attr.replace(b'\xee\xb9\x91', b'p')
            attr = attr.replace(b'\xef\x8d\x8e', b'J')
            attr = attr.replace(b'\xef\x8a\x8d', b'L')
            attr = attr.replace(b'\xee\x87\x9a', '生'.encode('utf-8'))
            attr = attr.replace(b'\xef\x95\xb5', '工'.encode('utf-8'))
            attr = attr.replace(b'\xef\x93\x9c', '程'.encode('utf-8'))
            attr = attr.replace(b'\xef\xa3\xba','师'.encode('utf-8'))
            attr = attr.replace(b'\xee\xba\x95','人'.encode('utf-8'))
            attr = attr.replace(b'\xee\x9a\x9e', '作'.encode('utf-8'))
            attr = attr.replace(b'\xee\xad\x85', '广'.encode('utf-8'))
            attr = attr.replace(b'\xef\x82\x8a', '设'.encode('utf-8'))
            attr = attr.replace(b'\xef\x92\x97', '计'.encode('utf-8'))
            attr = attr.replace(b'\xef\x9d\x80', '招'.encode('utf-8'))
            attr = attr.replace(b'\xee\x8b\x9d', '二'.encode('utf-8'))
            attr = attr.replace(b'\xee\xbf\x86', '互'.encode('utf-8'))
            attr = attr.replace(b'\xee\xbf\x86', '互'.encode('utf-8'))
            attr = attr.replace(b'\xef\xa1\xa5', '软'.encode('utf-8'))
            attr = attr.replace(b'\xee\x82\x86', '件'.encode('utf-8'))
            attr = attr.replace(b'\xef\xa1\xa5', '技'.encode('utf-8'))
            attr = attr.replace(b'\xef\xa1\xa5', '术'.encode('utf-8'))
            attr = attr.replace(b'\xee\x93\x8e', '市'.encode('utf-8'))
            attr = attr.replace(b'\xee\x94\x99', '场'.encode('utf-8'))
            attr = attr.replace(b'\xef\x80\x9c', '行'.encode('utf-8'))
            attr = attr.replace(b'\xee\xb4\x99', '告'.encode('utf-8'))
            attr = attr.replace(b'\xee\xa8\x86', '五'.encode('utf-8'))

            attr = attr.decode("utf-8")
            return attr
        item = BossjobItem()
        import chardet
        Jobs = response.xpath('//div[@class="clearfix intern-detail"]')
        for job in Jobs:
            name = job.xpath('div[@class="f-l intern-detail__job"]/p/a/text()')[0].extract()
            print(name)
            name = decode_num(self,name)
            address = job.xpath('div[@class="f-l intern-detail__job"]/p/span[@class="city ellipsis"]/text()')[0].extract()
            salary = job.xpath('div[@class="f-l intern-detail__job"]/p/span/text()')[0].extract()

            #decode(There are some anti-crawler mechanism in the website)
            salary = decode_num(self,salary)
            work_frequency = job.xpath('div[@class="f-l intern-detail__job"]/p/span[@class="font"]/text()')[0].extract()
            work_frequency = decode_num(self,work_frequency)

            work_period = job.xpath('div[@class="f-l intern-detail__job"]/p/span[@class="font"]/text()')
            if(len(work_period)>1):
                work_period = work_period[1].extract()
            else:
                work_period = ""
            work_period = decode_num(self,work_period)
            company_name = job.xpath('div[@class="f-r intern-detail__company"]/p/a/text()')[0].extract()
            company_employee_number = job.xpath('div[@class="f-r intern-detail__company"]/p/span[@class="font"]/text()')[0].extract()
            company_employee_number = decode_num(self,company_employee_number)
            detail_url = job.xpath('div[@class="f-l intern-detail__job"]/p/a/@href')[0].extract()

            item["Name"] = name
            item["Address"] = address
            item["Salary"] = salary
            item["Work_Frequency"] = work_frequency
            item["Work_Period"] = work_period
            item["Company_Name"] = company_name
            item["Company_Employee_Number"] = company_employee_number
            item["Detail_Url"] = detail_url
            yield item
        self.page += 1
        nextLink = "https://www.shixiseng.com/interns?page="+str(self.page)+"&type=intern&keyword=%E6%B8%B8%E6%88%8F&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
        if(self.page<15):
            time.sleep(5)
            yield Request(nextLink, callback=self.parse)






