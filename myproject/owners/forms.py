from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of owner:")
    id = IntegerField("ID of Puppy")
    submit = SubmitField("Add owner")