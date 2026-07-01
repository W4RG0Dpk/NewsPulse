from db.mongo import db

enriched_articles = db["enriched_articles"]


def search_titles(query, limit=10):

    tokens = [
        token.strip()
        for token in query.split()
        if token.strip()
    ]

    if not tokens:
        return []

    conditions = []

    for token in tokens:

        conditions.append(
            {
                "title": {
                    "$regex": rf"\b{token}\b",
                    "$options": "i"
                }
            }
        )

    results = enriched_articles.find(
        {
            "$or": conditions
        }
    ).limit(limit)

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
                "title",

            "score":
                None,

            "snippet":
                article["cleaned_content"][:250]
        })

    return output