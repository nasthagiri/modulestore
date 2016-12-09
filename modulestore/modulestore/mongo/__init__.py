"""
Provide names as exported by older mongo.py module
"""

from modulestore.mongo.base import MongoModuleStore, MongoKeyValueStore

# Backwards compatibility for prod systems that refererence
# modulestore.mongo.DraftMongoModuleStore
from modulestore.mongo.draft import DraftModuleStore as DraftMongoModuleStore
