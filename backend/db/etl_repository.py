from db.mongo import raw_articles


def get_unprocessed_articles(
    limit=5
):

    return raw_articles.find(
        {
            "processing_status.etl_completed": False
        }
    ).limit(limit)


def mark_etl_completed(
    article_id
):

    raw_articles.update_one(

        {
            "_id": article_id
        },

        {
            "$set": {
                "processing_status.etl_completed": True
            }
        }
    )