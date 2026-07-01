from search.entity_search import search_entities
from search.title_search import search_titles
from search.topic_search import search_topics
from search.semantic_search import semantic_search

from search.search_utils import (
    merge_results,
    deduplicate_results
)
def hybrid_search(query):

    entity_results = search_entities(query)

    title_results = search_titles(query)

    topic_results = search_topics(query)

    merged = merge_results(

        entity_results,

        title_results,

        topic_results

    )

    merged = deduplicate_results(merged)

    # -------------------------
    # Exact matches found
    # -------------------------

    if merged:

        return merged

    # -------------------------
    # Semantic fallback
    # -------------------------

    return semantic_search(query)