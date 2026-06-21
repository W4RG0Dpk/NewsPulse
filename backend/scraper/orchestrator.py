from scraper.pipeline_runner import run_pipeline
from scraper.rss_fetcher import RSS_FEEDS


def run_all_sources(limit=5):

    results = []

    total_inserted = 0
    total_skipped = 0
    total_failed = 0

    for source_name, feed_url in RSS_FEEDS.items():

        print(f"\nRunning {source_name}...")

        result = run_pipeline(
            source_name,
            feed_url,
            limit
        )

        results.append(result)

        total_inserted += result["inserted"]
        total_skipped += result["skipped"]
        total_failed += result["failed"]

    summary = {

        "sources_processed": len(results),

        "total_inserted": total_inserted,

        "total_skipped": total_skipped,

        "total_failed": total_failed,

        "results": results
    }

    return summary