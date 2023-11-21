from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Item {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            # "price": self.price
        }



# Here I am creating the database and tables
@app.route("/init")
def create_db():
    db.create_all()
    return "db created"


@app.route("/items", methods=["POST"])
def add_item():
    name = request.json.get("name")
    item = Item(name=name)
    print(item)
    print("BEFORE: ", item.to_dict())
    # return "testing"

    db.session.add(item)
    db.session.commit()
    print("AFTER: ", item.to_dict())
    return (
        jsonify({"message": "Item added", "item": {"id": item.id, "name": item.name}}),
        201,
    )


@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    items_squashed = [item.to_dict() for item in items]
    # print("ITEMS", items_squashed)

    # return items
    return jsonify({"items": [{"id": item.id, "name": item.name} for item in items]})


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({"item": {"id": item.id, "name": item.name}})


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.name = request.json.get("name", item.name)
    db.session.commit()
    return jsonify(
        {"message": "Item updated", "item": {"id": item.id, "name": item.name}}
    )


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)
