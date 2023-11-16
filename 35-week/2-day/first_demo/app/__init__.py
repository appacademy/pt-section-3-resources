from flask import Flask, render_template
from .posts import posts
from .routes.post_routes import post_routes
from .routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(post_routes, url_prefix="/posts")
app.register_blueprint(user_routes, url_prefix="/users")

@app.route("/")
def index():
    return render_template("index.html")
