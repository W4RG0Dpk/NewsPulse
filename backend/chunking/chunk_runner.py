from datetime import (
    datetime,
    timezone
)

from db.mongo import db

from db.chunk_repository import (
    save_chunks
)

from chunking.chunk_service import (
    create_chunks
)

enriched_articles = db[
    "enriched_articles"
]


def run_chunking(
    limit=5
):

    articles = list(

        enriched_articles.find()

        .limit(limit)
    )

    total_chunks = 0

    for article in articles:

        chunks = create_chunks(

            article[
                "cleaned_content"
            ]
        )

        documents = []

        for idx, chunk in enumerate(
            chunks,
            start=1
        ):

            documents.append({

                "article_id":
                    article["_id"],

                "chunk_id":
                    idx,

                "title":
                    article["title"],

                "source":
                    article["source"],

                "topic":
                    article["topic"],

                "chunk_text":
                    chunk,

                "chunk_length":
                    len(
                        chunk.split()
                    ),

                "embedding_generated":
                    False,

                "created_at":
                    datetime.now(
                        timezone.utc
                    )
            })

        save_chunks(
            documents
        )

        total_chunks += len(
            documents
        )

    return total_chunks