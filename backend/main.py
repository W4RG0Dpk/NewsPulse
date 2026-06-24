"""from db.mongo import raw_articles

result = raw_articles.delete_many({})

print(
    f"Deleted {result.deleted_count} documents"
)"""
"""To delete all doc in raw_articles"""

"""from db.mongo import db, raw_articles
from etl.etl_runner import run_etl

# ============================================================
# RESET ETL STATUS
# ============================================================

raw_articles.update_many(
    {},
    {
        "$set": {
            "processing_status.etl_completed": False
        }
    }
)

print("ETL flags reset.")

# ============================================================
# CLEAR ENRICHED COLLECTION
# ============================================================

delete_result = db["enriched_articles"].delete_many({})

print(
    f"Deleted {delete_result.deleted_count} enriched documents."
)

# ============================================================
# RUN ETL
# ============================================================

count = run_etl(limit=5)

print(f"\nProcessed {count} articles.")

# ============================================================
# VERIFY RESULTS
# ============================================================

print("\n")
print("=" * 80)
print("ENRICHED ARTICLE VERIFICATION")
print("=" * 80)

articles = list(
    db["enriched_articles"]
    .find()
    .limit(5)
)

for idx, article in enumerate(articles, start=1):

    print("\n")
    print("-" * 80)
    print(f"ARTICLE {idx}")
    print("-" * 80)

    print("\nTITLE:")
    print(article.get("title"))

    print("\nSOURCE:")
    print(article.get("source"))

    print("\nTOPIC:")
    print(article.get("topic"))

    print("\nSENTIMENT:")
    print(article.get("sentiment"))

    print("\nENTITY COUNT:")
    print(len(article.get("entities", [])))

    print("\nSAMPLE ENTITIES:")

    for entity in article.get("entities", [])[:5]:

        print(
            f"{entity['text']} "
            f"({entity['label']})"
        )

    print("\nCONTENT LENGTH:")
    print(
        len(
            article.get(
                "cleaned_content",
                ""
            )
        )
    )

# ============================================================
# ETL STATUS CHECK
# ============================================================

completed_count = raw_articles.count_documents(
    {
        "processing_status.etl_completed": True
    }
)

print("\n")
print("=" * 80)
print("ETL STATUS")
print("=" * 80)

print(
    f"ETL Completed Articles: "
    f"{completed_count}"
)"""

from analytics.entity_analytics import (
    get_top_entities
)

for item in get_top_entities():

    print(item)