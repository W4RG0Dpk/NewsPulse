from scraper.rss_fetcher import RSS_FEEDS, fetch_feed
from scraper.article_extractor import extract_article

from datetime import datetime
import hashlib


def build_article_document(metadata):

    extracted = extract_article(metadata["url"])

    if not extracted:
        return None

    content = extracted["content"]

    article_document = {

        "title": extracted["title"],

        "url": metadata["url"],

        "source": metadata["source"],

        "published_at": metadata["published_at"],

        "rss_id": metadata["rss_id"],

        "fetched_at": datetime.utcnow(),

        "content": content,

        "content_length": len(content),

        "content_hash": hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest(),

        "language": "en",

        "tags": [],

        "processing_status": {
            "etl_completed": False,
            "embedding_generated": False,
            "summary_generated": False
        }
    }

    return article_document

def build_articles_from_feed(
    source_name,
    feed_url,
    limit=5
):

    articles = fetch_feed(
        source_name,
        feed_url
    )

    documents = []

    for metadata in articles[:limit]:

        try:

            document = build_article_document(
                metadata
            )

            if document:
                documents.append(document)

        except Exception as e:

            print(
                f"Failed: {metadata['url']}"
            )

            print(e)

    return documents