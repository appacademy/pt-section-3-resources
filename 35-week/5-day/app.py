from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

# Session = sessionmaker(bind=engine)
# session = Session()

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(100), nullable=False)

    def hello(self):
        return "hello world"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


@app.route("/add_user/<username>")
def add_user(username):
    # db.create_all()
    new_user = User(name=username)

    print("New User", new_user)

    db.session.add(new_user)
    db.session.commit()
    return f"User {username} created!"


@app.route("/users")
def all_users():
    users = User.query.all()

    # print(users)
    # return users
    all_users = [user.to_dict() for user in users]

    return all_users



if __name__ == "__main__":
    app.run(debug=True)
