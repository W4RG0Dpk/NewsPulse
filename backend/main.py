from scraper.rss_fetcher import RSS_FEEDS, fetch_feed

for source, url in RSS_FEEDS.items():

    articles = fetch_feed(source, url)

    print("\n" + "="*60)
    print(source)
    print("="*60)

    print("Articles Found:", len(articles))

    if articles:

        print("\nFirst Article:\n")

        print(articles[0])