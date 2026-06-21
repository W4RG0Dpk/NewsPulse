"""from db.mongo import raw_articles

result = raw_articles.delete_many({})

print(
    f"Deleted {result.deleted_count} documents"
)"""
"""To delete all doc in raw_articles"""

from scraper.rss_fetcher import RSS_FEEDS
from scraper.scraper_service import (
    build_articles_from_feed
)

from db.article_repository import (
    save_many_articles
)

documents = build_articles_from_feed(
    "TheHindu",
    RSS_FEEDS["TheHindu"],
    limit=5
)

result = save_many_articles(
    documents
)

print("\nPIPELINE RESULT")

print(
    f"Inserted : {result['inserted']}"
)

print(
    f"Skipped  : {result['skipped']}"
)