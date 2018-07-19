from flask_table import Table, Col, BoolCol, ButtonCol

class ItemTable(Table):
    classes = ['table table-striped']
    thead_classes = ['thead-dark']
    _id = Col('Name')
    art = Col('Klasse')
    kind = Col('Art')
    haveit = BoolCol('Vorhanden', yes_display='ja', no_display='nein')
    changeit = ButtonCol('ändern', 'update', url_kwargs=dict(id = "_id",richtung="haveit"))


