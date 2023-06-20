"""Example of a python flask api
"""
import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items

app = Flask(__name__)


############################ stores ################################
@app.get("/store")
def get_stores():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"stores": list(stores.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    """_summary_

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        return stores[store_id], 201
    except KeyError:
        abort(404, message="Store not found")


@app.post("/store")
def create_store():
    """_summary_

    Returns:
        _type_: _description_
    """
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad Request, Ensure 'name is inlcuded in the json payload")
    for store in stores.values():
        if store_data["name"] in store["name"]:
            abort(400, "Store already exists")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    """_summary_

    Args:
        store_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        del stores[store_id]
        return {"message": "Store deleted"}
    except KeyError:
        abort(400, message="Store not found")
    return stores, 200


################################## items ######################################


@app.get("/item")
def get_all_items():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_item(item_id):
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


@app.post("/item")
def create_item():
    """_summary_

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    item_data = request.get_json()
    if (
        "name" not in item_data
        or "price" not in item_data
        or "store_id" not in item_data
    ):
        abort(
            400,
            message="Ensure 'price','store_id' and 'name' to be included in the json payload",
        )
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
    for item in items.values():
        if (
            item_data["name"] in item["name"]
            and item_data["store_id"] in item["store_id"]
        ):
            abort(400, message="Same item is present in the store")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201  # 201 is created success


@app.put("/item/<string:item_id>")
def update_item(item_id):
    """_summary_

    Args:
        store_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(
            400,
            message="Bad request, Ensure 'price' and 'name' to be included in the JSON paylod",
        )
    try:
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        abort(404, message="item id not found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    """_summary_

    Args:
        item_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, message="Item not found")
