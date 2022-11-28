from scrapy.cmdline import execute

execute("scrapy crawl JobBoss -o bossjob.json -s FEED_EXPORT_ENCODING=utf-8".split())