import time

from datetime import datetime, timezone

from scraper.rss_fetcher import fetch_feed
from scraper.scraper_service import build_article_document

from db.article_repository import save_many_articles
from db.log_repository import save_scrape_log
from db.error_repository import save_error


def run_pipeline(
    source_name,
    feed_url,
    limit=5
):

    started_at = datetime.now(
        timezone.utc
    )

    start_time = time.time()

    articles = fetch_feed(
        source_name,
        feed_url
    )

    documents = []

    failed = 0

    for metadata in articles[:limit]:

        try:

            document = build_article_document(metadata)
           

            if document:

                documents.append(
                    document
                )

        except Exception as e:

            failed += 1
            save_error({

                "source": source_name,

                "url": metadata["url"],

                "error": str(e),

                "timestamp": datetime.now(
                    timezone.utc
                )
            })

    save_result = save_many_articles(
        documents
    )

    runtime = round(
        time.time() - start_time,
        2
    )

    finished_at = datetime.now(
        timezone.utc
    )

    log_document = {

        "source": source_name,

        "articles_found": len(
            articles
        ),

        "articles_processed": len(
            documents
        ),

        "inserted": save_result[
            "inserted"
        ],

        "skipped": save_result[
            "skipped"
        ],

        "failed": failed,

        "runtime_seconds": runtime,

        "started_at": started_at,

        "finished_at": finished_at
    }

    save_scrape_log(
        log_document
    )

    return log_document