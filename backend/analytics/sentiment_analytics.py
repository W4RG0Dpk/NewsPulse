from db.mongo import db

enriched_articles = db[
    "enriched_articles"
]


def get_sentiment_distribution():

    pipeline = [

        {
            "$group": {

                "_id":
                    "$sentiment.label",

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

    return list(
        enriched_articles.aggregate(
            pipeline
        )
    )