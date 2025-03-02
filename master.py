from DbScraper.google_search import GoogleSearch

sources = [e.rstrip('\n') for e in open('sources.txt', 'r', encoding='utf-8').readlines()]
countries = [e.rstrip('\n') for e in open('countries.txt', 'r', encoding='utf-8').readlines()]
keywords = [e.rstrip('\n') for e in open('keywords.txt', 'r', encoding='utf-8').readlines()]

GoogleSearch(countries[0] + keywords[0], num_results=1, depth=1, timeout=10).start()
# print(sources)

# process = CrawlerProcess(get_project_settings())

# process = CrawlerProcess(
#     settings={
#         "FEEDS": {
#             "items.json": {"format": "json"},
#         },
#     }
# )

# process.crawl(MySpider)
# process.start()