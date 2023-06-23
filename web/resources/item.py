import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schema import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on store items")


@blp.route("/item")
class ItemList(MethodView):
    """_summary_

    Args:
        MethodView (_type_): _description_
    """

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return list(items.values())

    @blp.arguments(ItemSchema)
    @blp.response(200,ItemSchema)
    def post(self, item_data):
        """_summary_

        Args:
            item_data (_type_): _description_

        Returns:
            _type_: _description_
        """
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


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    """_summary_

    Args:
        MethodView (_type_): _description_
    """

    @blp.response(200, ItemSchema)
    def get(self, item_id):
        """_summary_

        Args:
            item_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        """_summary_

        Args:
            item_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            del items[item_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(400, message="Store not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        """_summary_

        Args:
            item_data (_type_): _description_
            item_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="item id not found")
