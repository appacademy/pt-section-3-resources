from flask import Blueprint, render_template
from ..posts import posts
from ..forms.post import PostForm

post_routes = Blueprint("taco", __name__)

@post_routes.route("/all")
def get_posts():
    print("POSTS: ", posts)
    # request comes in from the frontend..probably your redux thunk
    # Query my database
    # send query results to frontend
    return render_template("posts.html", posts=posts)


@post_routes.route("/posts", methods=["GET", "POST"])
def add_post():
    print("POSTS: ", posts)
    form = PostForm()
    if form.validate_on_submit():
        new_post = {
            "author": form.data["author"]
        }
        print("New Post!", new_post)
        posts.append(new_post)

    return render_template("posts.html", posts=posts)
