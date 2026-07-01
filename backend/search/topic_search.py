from db.mongo import db

enriched_articles = db[
    "enriched_articles"
]


def search_topics(
    query,
    limit=10
):

    return list(

        enriched_articles.find(

            {
                "topic": {
                    "$regex": query,
                    "$options": "i"
                }
            }

        ).limit(limit)
    )