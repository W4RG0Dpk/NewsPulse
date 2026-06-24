from db.mongo import db

enriched_articles = db["enriched_articles"]


def get_topic_distribution():

    pipeline = [

        {
            "$group": {
                "_id": "$topic",
                "count": {
                    "$sum": 1
                }
            }
        },

        {
            "$sort": {
                "count": -1
            }
        }
    ]

    results = list(
        enriched_articles.aggregate(
            pipeline
        )
    )

    return results