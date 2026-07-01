import numpy as np

from embeddings.embedding_service import (
    generate_embedding
)

from db.mongo import db

article_chunks = db[
    "article_chunks"
]


def cosine_similarity(
    vec1,
    vec2
):

    vec1 = np.array(vec1)

    vec2 = np.array(vec2)

    return np.dot(
        vec1,
        vec2
    ) / (

        np.linalg.norm(vec1)

        *

        np.linalg.norm(vec2)
    )


def semantic_search(
    query,
    top_k=5
):

    query_embedding = (
        generate_embedding(
            query
        )
    )

    results = []

    chunks = article_chunks.find(
        {
            "embedding_generated":
                True
        }
    )

    for chunk in chunks:

        score = cosine_similarity(

            query_embedding,

            chunk["embedding"]
        )

        results.append({

            "article_id":
                str(chunk["article_id"]),

            "title":
                chunk["title"],

            "source":
                chunk["source"],

            "topic":
                chunk["topic"],

            "strategy":
                "semantic",

            "score":
                float(score),

            "snippet":
                chunk["chunk_text"][:250]
        })

    results.sort(

        key=lambda x:
            x["score"],

        reverse=True
    )

    return results[:top_k]