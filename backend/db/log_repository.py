from db.mongo import scrape_logs


def save_scrape_log(log_document):

    result = scrape_logs.insert_one(
        log_document
    )

    return result.inserted_id