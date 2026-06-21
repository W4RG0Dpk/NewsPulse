from db.mongo import raw_articles


def article_exists(content_hash):

    return raw_articles.find_one(
        {
            "content_hash": content_hash
        }
    )


def save_article(article_document):

    existing = article_exists(
        article_document["content_hash"]
    )

    if existing:

        return None

    result = raw_articles.insert_one(
        article_document
    )

    return result.inserted_id
def save_many_articles(documents):

    inserted = 0
    skipped = 0

    for document in documents:

        if article_exists(
            document["content_hash"]
        ):

            skipped += 1

            continue

        raw_articles.insert_one(
            document
        )

        inserted += 1

    return {
        "inserted": inserted,
        "skipped": skipped
    }