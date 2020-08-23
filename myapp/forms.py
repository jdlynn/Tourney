from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CustomUserProfileForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    phone_no = StringField('Phone No')
    address = StringField('Street Address')
    city = StringField('City')
    state = StringField('State')
    zipcode = StringField('Zip Code')
    submit = SubmitField('Update')


class TeamForm(FlaskForm):
    teamname = StringField('Team Name', validators=[DataRequired()])
    seed = IntegerField('Seed', validators=[DataRequired()])
    region_select = SelectField('Region', coerce=int)
    submit = SubmitField('Sign In')