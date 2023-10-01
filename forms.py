from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for Adding Pets"""
    name = StringField("Pet Name", validators=[InputRequired])

    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form to Edit an Existing Pet"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")








                                         




