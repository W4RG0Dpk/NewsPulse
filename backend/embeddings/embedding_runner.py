from embeddings.embedding_service import (
    generate_embedding
)

from db.embedding_repository import (

    get_chunks_without_embeddings,

    save_embedding
)


def run_embeddings(
    limit=10
):

    chunks = (
        get_chunks_without_embeddings(
            limit
        )
    )

    processed = 0

    for chunk in chunks:

        embedding = generate_embedding(

            chunk[
                "chunk_text"
            ]
        )

        save_embedding(

            chunk["_id"],

            embedding
        )

        processed += 1

    return processed