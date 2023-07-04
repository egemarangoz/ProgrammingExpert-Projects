"""
Assessment 4.5 - Asynchronous Fethcer

Write a "BatchFetcher" class that is meant to fetch lots of records from a database very quickly.

Your constructor takes in a "database" object that has a "sync" method called "async_fetch". This method takes a record identifier (or record_id)
and returns watever the database has in storage for that record.

"BatchFetcher" should implement the async method "fetch_records", which takes in a list, "records_id", and should return the list of records
corresponding to those "record_ids".

"""
import asyncio


class BatchFetcher:
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        pending_records = []
        for record_id in record_ids:
            pending_records.append(self.database.async_fetch(record_id))

        return await asyncio.gather(*pending_records)
