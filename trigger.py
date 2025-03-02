from scrapy.crawler import CrawlerProcess
import argparse
import uuid

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('--url')
parser.add_argument('--depth', default=3, type=int)
parser.add_argument('--timeout', default=600, type=int)
parser.add_argument('--output', default=f"data-{uuid.uuid4().hex[:6].upper()}.csv")

args = parser.parse_args()

# config = get_project_settings()
config = dict()
config["SPIDER_MODULES"] = "DbScraper.spiders"
config["DEPTH_LIMIT"] = args.depth
config["CLOSESPIDER_TIMEOUT"] = args.timeout
config["FEEDS"] = {
    args.output: {
        'format': 'csv',
        'encoding': 'utf8',
        'overwrite': False,
    }
}

process = CrawlerProcess(config)
process.crawl("LinkSpider", 
                  start_urls=[args.url])
process.start()
