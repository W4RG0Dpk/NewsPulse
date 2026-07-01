from db.mongo import db

article_chunks = db[
    "article_chunks"
]


def save_chunks(chunks):

    if not chunks:
        return

    article_chunks.insert_many(
        chunks
    )