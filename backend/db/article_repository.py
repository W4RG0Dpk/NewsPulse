from db.mongo import raw_articles


def save_article(article_document):

    result = raw_articles.insert_one(
        article_document
    )

    return result.inserted_id