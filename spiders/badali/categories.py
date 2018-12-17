import json
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # http://badali.umh.es/models/funciones.php?funcion=listarsubgruposexistentes
    start_urls = [
        'http://badali.umh.es/models/funciones.php?funcion=listargruposexistentes'
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        subgroups = scrapy.Request(url="http://badali.umh.es/models/funciones.php?funcion=listargruposexistentes", callback=self.subgroups_processor)
        for sub in subgroups:
            yield {
                'a': 1
            }
        for group in jsonresponse:
            group_id = group["id"],
            yield {
                'id': group_id,
                'name': group["nombre"]
            }

    def subgroups_processor(self, response):
        print(response)
        yield response
