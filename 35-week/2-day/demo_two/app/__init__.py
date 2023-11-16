import sqlite3
from flask import Flask, render_template, redirect
from .config import Config
from .forms.create_patient import PatientForm
from .routes.patients import patient_routes

DB_FILE = "../dev.db"
with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS patients;")
    curs.execute(
        """
        CREATE TABLE patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
        );
        """
    )
    curs.execute(
        """
        INSERT INTO patients (first_name, last_name, email)
        VALUES
        ('Tim', 'Petrol', 'rotary@fast.com'),
        ('Ryan', 'Runner', '10sec@jdm.com'),
        ('Tia', 'Petrol', 'typer@wtec.com');
        """
    )

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def get_index():
    return render_template("index.html", page="HOME", sitename="Patient Tracker")


@app.route("/", methods=["GET"])
def get_all_patients():
    patiend_id = request.args.get("id")
    if patiend_id is not None:
        return redirect(f"/patients/{patiend_id}")

    patients = None
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute("SELECT * FROM patients;")
        result = curs.fetchall()
        if len(result) > 0:
            patients = result
    if patients is not None:
        return render_template(
            "all_patients.html",
            page="All Patients",
            sitename="Patient Tracker",
            patients=patients,
        )
    else:
        return "No Patients exist!"

app.register_blueprint(patient_routes, url_prefix='/patients')

# @app.route("/<int:id>", methods=["GET"])
# def get_one_patient(id):
#     patient = None
#     with sqlite3.connect(DB_FILE) as conn:
#         curs = conn.cursor()
#         curs.execute(f"SELECT * FROM patients WHERE id={id};")
#         result = curs.fetchone()
#         patient = result
#     if patient is not None:
#         return render_template("one_patient.html", patient=patient), 200
#     else:
#         return render_template("one_patient.html", patient="Patient Not Found"), 404


# @app.route("/create", methods=["GET"])
# def get_create_patient_form():
#     form = PatientForm()
#     return render_template("create_patient.html", form=form)


# @app.route("/", methods=["POST"])
# def post_patient():
#     form = PatientForm()
#     if form.validate_on_submit():
#         with sqlite3.connect(DB_FILE) as conn:
#             curs = conn.cursor()
#             curs.execute(
#                 """INSERT INTO patients (first_name, last_name, email)
#         VALUES (?, ?, ?)""",
#                 (form.data["first_name"], form.data["last_name"], form.data["email"]),
#             )
#         return redirect("/patients")
#     else:
#         return render_template("create_patient.html", form=form)
