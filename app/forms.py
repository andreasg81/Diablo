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
    filt_avaclass = SelectField('Charakter', choices=[('Alle', 'Alle')] + Config.AVATARS)
    filt_itemclass = SelectField('Art', choices=[('Alle', 'Alle')] + Config.ITEM_KIND)
    filt_have_it = SelectField('Vorhanden', choices=[('Alle', 'Alle'), ('Vorhanden', 'Vorhanden'), ('Fehlt', 'Fehlt')])
    submit = SubmitField('Filtern')