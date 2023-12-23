from flask import Blueprint, render_template, redirect
from app.forms import SimpleForm
from app.models import SimplePerson, db


bp = Blueprint("simple", __name__)

@bp.route('/')
def index():
    return render_template("main_page.html")

@bp.route('/simple-form')
def get_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)

@bp.route('/simple-form', methods=['POST'])
def post_data():
    form = SimpleForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        bio = form.bio.data

        new_person = SimplePerson(name=name, age=age, bio=bio)

        db.session.add(new_person)
        db.session.commit()
        return redirect('/')
    return "Bad Data"

@bp.route("/simple-form-data")
def get_data():
    people = SimplePerson.query.filter(SimplePerson.name.like("M%"))
    return render_template("simple_form_data.html", people=people)
