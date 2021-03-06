from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
#from ..models import Achievement, User


class AchievementForm(FlaskForm):
    achievement = StringField('Achievement:', validators=[DataRequired()])
    isComplete = BooleanField('Completed?')
    progress = StringField('Progress')
    submit = SubmitField('Add!')

class EditAchievementForm(FlaskForm):
    achievement = StringField('Add a new achievement:', validators=[DataRequired()])
    isComplete = BooleanField('Completed?')
    progress = StringField('Progress')
    submit = SubmitField('Update!')
    cancel = SubmitField('Cancel')

