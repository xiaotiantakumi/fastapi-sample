import os
from azure.cosmos.cosmos_client import CosmosClient


def get_owners():
    url = os.environ["AZURE_COSMOS_DUMMYDB_URI"]
    credential = os.environ["AZURE_COSMOS_DUMMYDB_KEY"]

    client = CosmosClient(url, credential)
    database_id = 'DummyDB'
    container_id = 'M_OWNER'
    datebase = client.get_database_client(database=database_id)
    container = datebase.get_container_client(container=container_id)

    query = "SELECT c['owner_id'], c['owner_name'] FROM c"
    return container.query_items(query=query, enable_cross_partition_query=True)


def get_owner_name(owner_id: str):
    url = os.environ["AZURE_COSMOS_DUMMYDB_URI"]
    credential = os.environ["AZURE_COSMOS_DUMMYDB_KEY"]

    client = CosmosClient(url, credential)
    database_id = 'DummyDB'
    container_id = 'M_OWNER'
    datebase = client.get_database_client(database=database_id)
    container = datebase.get_container_client(container=container_id)

    query = "SELECT c['owner_name'] FROM c where c['owner_id'] = @owner_id"
    parameters: list[dict[str, object]] = [{"name": "@owner_id", "value": owner_id}]
    items = container.query_items(query, parameters, enable_cross_partition_query=True)
    owners = list(items)

    if len(owners) == 0:
        return ''
    else:
        owner_name = owners[0]['owner_name']
        return owner_name
