from db.mongo import db

enriched_articles = db["enriched_articles"]


def search_entities(query, limit=10):

    # ----------------------------------------
    # Split query into individual tokens
    # ----------------------------------------

    tokens = [

        token.strip()

        for token in query.split()

        if token.strip()
    ]

    # Empty query

    if not tokens:

        return []

    # ----------------------------------------
    # Build OR conditions
    # ----------------------------------------

    conditions = []

    for token in tokens:

        conditions.append(

            {
                "entities.text": {

                    "$regex": rf"\b{token}\b",

                    "$options": "i"
                }
            }
        )

    # ----------------------------------------
    # Mongo Query
    # ----------------------------------------

    results = enriched_articles.find(

        {
            "$or": conditions
        }

    ).limit(limit)

    # ----------------------------------------
    # Normalize Output
    # ----------------------------------------

    output = []

    for article in results:

        output.append({

            "article_id":
                str(article["_id"]),

            "title":
                article["title"],

            "source":
                article["source"],

            "topic":
                article["topic"],

            "strategy":
                "entity",

            "score":
                None,

            "snippet":
                article[
                    "cleaned_content"
                ][:250]
        })

    return output