from db.mongo import db

enriched_articles = db[
    "enriched_articles"
]


def get_top_entities(limit=10):

    pipeline = [

        {
            "$unwind":
                "$entities"
        },

        {
            "$group": {

                "_id":
                    "$entities.text",

                "count": {
                    "$sum": 1
                }
            }
        },

        {
            "$sort": {
                "count": -1
            }
        },

        {
            "$limit":
                limit
        }
    ]

    return list(
        enriched_articles.aggregate(
            pipeline
        )
    )