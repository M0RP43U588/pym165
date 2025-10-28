from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor
from shared.data import filter_type, actual_doc_type, collection_fields

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
    return bool(get_collection().insert_one(filters).inserted_id)


def mongodb_update(filters: filter_type, change: actual_doc_type) -> bool:
    result = get_collection().update_one(filters, change)
    return result.matched_count > 0


def mongodb_delete(filters: filter_type) -> bool:
    result = get_collection().delete_one(filters)
    return result.deleted_count > 0


def document_field_validator(value: str) -> bool:
    return bool(value.strip() in collection_fields)
