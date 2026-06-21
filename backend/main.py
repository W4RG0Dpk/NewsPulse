from scraper.rss_fetcher import RSS_FEEDS, fetch_feed
from scraper.scraper_service import build_article_document

from db.article_repository import save_article

articles = fetch_feed(
    "TheHindu",
    RSS_FEEDS["TheHindu"]
)

document = build_article_document(
    articles[0]
)

inserted_id = save_article(document)

print("Inserted:", inserted_id)