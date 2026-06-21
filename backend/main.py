"""from scraper.rss_fetcher import RSS_FEEDS, fetch_feed

for source, url in RSS_FEEDS.items():

    articles = fetch_feed(source, url)

    print("\n" + "="*60)
    print(source)
    print("="*60)

    print("Articles Found:", len(articles))

    if articles:

        print("\nFirst Article:\n")

        print(articles[0])"""
from scraper.rss_fetcher import RSS_FEEDS, fetch_feed
from scraper.article_extractor import extract_article

source = "TheHindu"

articles = fetch_feed(source, RSS_FEEDS[source])

first_article = articles[0]

print("\nURL:")
print(first_article["url"])

result = extract_article(first_article["url"])

print("\nTitle:")
print(result["title"])

print("\nContent Length:")
print(result["content_length"])

print("\nSample:")
print(result["content"][:500])