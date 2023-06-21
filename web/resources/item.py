import uuid
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schema import ItemSchema, ItemUpdateSchema
blp = Blueprint("Items",__name__,description="Operations on store items")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}
    
    @blp.arguments(ItemSchema)
    def post(self, item_data):
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
        for item in items.values():
            if (
                item_data["name"] in item["name"]
                and item_data["store_id"] in item["store_id"]
                ):
                abort(400, message="Same item is present in the store")
        item_id = uuid.uuid4().hex
        item = { **item_data, "id": item_id}
        items[item_id] = item
        return item, 201  # 201 is created success

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(400, message="Store not found")
    @blp.arguments(ItemUpdateSchema)
    def put(self,item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="item id not found")

