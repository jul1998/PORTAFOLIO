from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    repo = StringField('repo', validators=[DataRequired()])
    img = TextAreaField('img', validators=[DataRequired()])
    group = StringField('group', validators=[DataRequired()])