from db.etl_repository import (
    get_unprocessed_articles,
    mark_etl_completed
)

from db.enriched_repository import (
    save_enriched_article
)
from etl.text_cleaner import (
    clean_text
)
from etl.ner_extractor import (
    extract_entities
)
from etl.sentiment_analyzer import (
    analyze_sentiment
)
from etl.topic_classifier import (
    classify_topic
)

def run_etl(limit=5):

    articles = (
        get_unprocessed_articles(
            limit
        )
    )

    processed = 0

    for article in articles:
        cleaned_content = clean_text(article["content"])
        entities = extract_entities(cleaned_content)
        sentiment = analyze_sentiment(cleaned_content)
        topic = classify_topic(cleaned_content)


        enriched_document = {

            "article_id":
                article["_id"],

            "title":
                article["title"],

            "source":
                article["source"],
            "entities": entities,
            "sentiment": sentiment,
            "topic": topic,

            "cleaned_content":
                cleaned_content,

            "processed_at":
                article["fetched_at"],

            "processing_version":
                "v1"
        }

        save_enriched_article(
            enriched_document
        )

        mark_etl_completed(
            article["_id"]
        )

        processed += 1

    return processed