from apscheduler.schedulers.blocking import BlockingScheduler

from scraper.orchestrator import (
    run_all_sources
)

scheduler = BlockingScheduler()

# change timer here 
@scheduler.scheduled_job(
    "interval",
  #  hours=1
  seconds=30
)
def scheduled_ingestion():

    print(
        "\nRunning Scheduled Ingestion..."
    )

    run_all_sources(limit=5)


def start_scheduler():

    print(
        "Scheduler Started..."
    )

    scheduler.start()