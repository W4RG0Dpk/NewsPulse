from db.mongo import db

error_logs = db["error_logs"]


def save_error(error_document):

    result = error_logs.insert_one(
        error_document
    )

    return result.inserted_id