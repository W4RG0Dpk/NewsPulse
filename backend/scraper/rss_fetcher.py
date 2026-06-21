import feedparser

RSS_FEEDS = {
    "TheHindu": "https://www.thehindu.com/news/feeder/default.rss",
    "TechCrunch": "https://techcrunch.com/feed/"
}


def fetch_feed(source_name, feed_url):

    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:

        articles.append({
            "title": entry.get("title"),
            "url": entry.get("link"),
            "source": source_name,
            "published_at": entry.get("published"),
            "rss_id": entry.get("id", entry.get("link"))
        })

    return articles