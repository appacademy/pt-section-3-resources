from flask import Blueprint, render_template


user_routes = Blueprint("users", __name__)

@user_routes.route("/")
def get_will():
    # request comes in from the frontend..probably your redux thunk
    # Query my database
    # send query results to frontend
    return f"<h1>Will is the user</h1>"
