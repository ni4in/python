import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schema import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store")
class StoreList(MethodView):
    """_summary_

    Args:
        MethodView (_type_): _description_
    """
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return list(stores.values())

    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self, store_data):
        """_summary_

        Args:
            store_data (_type_): _description_

        Returns:
            _type_: _description_
        """
        for store in stores.values():
            if store_data["name"] in store["name"]:
                abort(400, "Store already exists")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201


@blp.route("/stores/<string:store_id>")
class Store(MethodView):
    """_summary_

    Args:
        MethodView (_type_): _description_
    """
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        """_summary_

        Args:
            store_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            return stores[store_id], 201
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
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
