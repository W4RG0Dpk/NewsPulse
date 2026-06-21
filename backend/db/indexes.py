from db.mongo import raw_articles


def create_indexes():

    raw_articles.create_index(
        "content_hash",
        unique=True
    )

    print(
        "Indexes created successfully"
    )