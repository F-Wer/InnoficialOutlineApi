import requests

apiurl = "https://api.outline.com/v3/parse_article?source_url=" # Hardcoded API URL; got it via network tools in the browser
url = "https://outline.com/" # main url

def parse_url(url): # sends the url to the API and returns the response
        r = requests.get(apiurl + url)
        data = r.json()['data']['short_code']
        if data == 'not_supported' or data == '': # if the API returns not_supported or empty, it means the article is not supported
            raise ExceptionOutline('Not supported or not found')
        return data

class ExceptionOutline(Exception): # custom exception
    pass
