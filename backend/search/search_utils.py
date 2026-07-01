def merge_results(*result_lists):

    merged = []

    for results in result_lists:

        merged.extend(results)

    return merged


def deduplicate_results(results):

    unique = {}

    for article in results:

        article_id = article["article_id"]

        # Keep first occurrence

        if article_id not in unique:

            unique[article_id] = article

    return list(unique.values())