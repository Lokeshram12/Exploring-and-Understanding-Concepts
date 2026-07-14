import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.status_code

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url) 
    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/lru-cache-python/")
get_article("https://realpython.com/sorting-algorithms-python/")

print(cache)