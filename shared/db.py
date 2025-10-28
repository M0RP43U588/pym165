from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor
from shared.data import filter_type, actual_doc_type

CLIENT: MongoClient | None = None


def init_client() -> MongoClient:
    global CLIENT
    if CLIENT is None:
        CLIENT = MongoClient("mongodb://localhost:27017")
    return CLIENT


def get_db() -> Database:
    return init_client()["kinofilme"]


def get_collection() -> Collection:
    return get_db()["dvd_sammlung"]


def mongodb_read(filters: filter_type) -> Cursor:
    return get_collection().find(filters)


def mongodb_create(filters: actual_doc_type) -> bool:
    return get_collection().insert_one(filters).acknowledged
