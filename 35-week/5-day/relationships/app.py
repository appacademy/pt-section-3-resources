from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)

likes = db.Table(
    "likes",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    posts = db.relationship("Post", back_populates="user")
    post_likes = db.relationship("Post", secondary=likes, back_populates="user_likes")


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")
    user_likes = db.relationship("User", secondary=likes, back_populates="post_likes")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(120), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

    post = db.relationship("Post", back_populates="comments")


@app.before_request
def init_db():
    db.drop_all()
    db.create_all()

    will = User(name="Will")
    sally = User(name="Sally")
    bobby = User(name="Bobby")
    db.session.add(will)
    db.session.add(sally)
    db.session.add(bobby)
    db.session.commit()

    all_users = User.query.all()

    # will's post
    post = Post(title="Hello, world!", user_id=will.id)
    db.session.add(post)
    db.session.commit()


    if sally not in post.user_likes and bobby not in post.user_likes:
        post.user_likes.append(sally)
        post.user_likes.append(bobby)
        db.session.commit()
    else:
        print("user already liked this post!")

    comment = Comment(caption="awesome!", post_id=post.id)
    db.session.add(comment)
    db.session.commit()


@app.route("/")
def index():

    post = Post.query.first()

    for p in post.user_likes:
        print(f"{p.name} liked your post")

    return "Welcome to the Flask-SQLAlchemy demo!"


if __name__ == "__main__":
    app.run(debug=True)
