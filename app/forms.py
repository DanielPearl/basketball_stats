from app import app, models, db, queries
from wtforms import Form, SubmitField, SelectField, SelectMultipleField, validators, ValidationError
from wtforms.validators import Required, Optional, NumberRange, DataRequired, Length, Email, EqualTo

from .queries import *

class TeamForm(Form):
    team_choices = queries.get_team_choices()
    year_choices = queries.get_year_choices()

    team1 = SelectField('Team 1', choices=team_choices, default="", validators = [Required()])

    team2 = SelectField('Team 2', choices=team_choices, default="", validators = [Required()])

    year = SelectField('Year', choices=year_choices, default="", validators = [Required()])
    submit = SubmitField('Submit')
