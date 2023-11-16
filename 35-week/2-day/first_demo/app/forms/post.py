from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


# def my_length_check(form, field):
    # if len(field.data) > 50:
    #     raise ('Field must be less than 50 characters')


class PostForm(FlaskForm):
    author = StringField("Author", validators=[DataRequired(), Length(min=5)])
