from db.mongo import db

enriched_articles = db[
    "enriched_articles"
]


def get_source_distribution():

    pipeline = [

        {
            "$group": {

                "_id":
                    "$source",

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