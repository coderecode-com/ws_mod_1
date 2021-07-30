import requests
import scraper_helper

headers = scraper_helper.get_dict('''
   Accept: */*  
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: __utma=149486891.600689303.1627644443.1627644443.1627644443.1; __utmc=149486891; __utmz=149486891.1627644443.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=149486891.1.10.1627644443; PHPSESSID=180mrglusc6pe4o3n01n5qu80b0u9n74
    Host: librivox.org
    Pragma: no-cache
    Referer: https://librivox.org/search/?search_form=get_results&q=The%20Secret%20Garden
    sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
    sec-ch-ua-mobile: ?0
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
    X-Requested-With: XMLHttpRequest
    '''
)
url='https://librivox.org/advanced_search?title=&author=&reader=&keywords=&genre_id=0&status=all&project_type=either&recorded_language=&sort_order=alpha&search_page=1&search_form=advanced&q=The%20Secret%20Garden'
response = requests.get(url,headers=headers)

print(type(response.json()))