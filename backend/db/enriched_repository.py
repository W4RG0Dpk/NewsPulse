from db.mongo import db

enriched_articles = db[
    "enriched_articles"
]


def save_enriched_article(
    document
):

    result = (
        enriched_articles
        .insert_one(document)
    )

    return result.inserted_id