from db.mongo import db

article_chunks = db[
    "article_chunks"
]


def get_chunks_without_embeddings(
    limit=10
):

    return article_chunks.find(
        {
            "embedding_generated":
                False
        }
    ).limit(limit)


def save_embedding(
    chunk_id,
    embedding
):

    article_chunks.update_one(

        {
            "_id": chunk_id
        },

        {
            "$set": {

                "embedding":
                    embedding,

                "embedding_generated":
                    True
            }
        }
    )