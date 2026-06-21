"""from db.mongo import raw_articles

result = raw_articles.delete_many({})

print(
    f"Deleted {result.deleted_count} documents"
)"""
"""To delete all doc in raw_articles"""

from scheduler.scheduler_service import (
    start_scheduler
)

start_scheduler()