from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired
from config import Config

#TODO Form für Einschrencken bauen
class ItemForm(FlaskForm):
    itemname = StringField('Item', validators=[DataRequired()])
    avaclass = SelectMultipleField('Charakter', choices=Config.AVATARS)
    itemclass = SelectField('Art', choices=Config.ITEM_KIND)
    have_it = BooleanField('Vorhanden')
    submit = SubmitField('Speichern')

class FilterItem(FlaskForm):
    avaclass = SelectField('Charakter', choices=Config.AVATARS)
    have_it = BooleanField('Vorhanden')
    submit = SubmitField('Filtern')