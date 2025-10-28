from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

CLIENT: MongoClient | None = None


def init_client() -> MongoClient:
    global CLIENT
    if CLIENT is None:
        CLIENT = MongoClient("mongodb://localhost:27017")
    return CLIENT


def get_db() -> Database:
    return init_client()["filme"]


def get_collection() -> Collection:
    return get_db()["dvd_sammlung"]


def mongodb_read(collection: Collection,
                 filters: dict[str, str | int | float]) -> dict[str, str | int | float | list]:
    return collection.find(filters)
