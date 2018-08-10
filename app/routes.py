from app import app
from flask import render_template, flash, redirect, session
from app.forms import ItemForm, FilterItem
from app.modules import item
from app.tabels import ItemTable

@app.route('/get')
def get():
    return str(session.get('have_it', 'nix'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    session.permanent = True
    form = ItemForm()
    form2 = FilterItem()
    if form.validate_on_submit():
        newItem = item()
        newItem.save_item(form.itemname.data,form.avaclass.data, form.itemclass.data, form.have_it.data)
        return redirect('/index')
    if form2.validate_on_submit():
        session['have_it'] = form2.filt_have_it.data
        session['itemclass'] = form2.filt_itemclass.data
        session['avaclass'] = form2.filt_avaclass.data
        filterItem = item()
        filter = {}
        if form2.filt_have_it.data != 'Alle':
            if form2.filt_have_it.data == "Fehlt":
                filter.update({"haveit":False})
            else:
                filter.update({"haveit": True})
        if form2.filt_itemclass.data != "Alle":
            filter.update({'kind':form2.filt_itemclass.data})
        if form2.filt_avaclass.data != "Alle":
            filter.update({'art':form2.filt_avaclass.data})
        session['filter'] = filter
        #data = filterItem.filter(filter)
        #tabel = ItemTable(data)
        #return render_template('index.html', title='Home', form=form, form2=form2, tabel=tabel)
    form2.filt_have_it.default = session.get('have_it', "Alle")
    form2.filt_avaclass.default = session.get('avaclass', "Alle")
    form2.filt_itemclass.default = session.get('itemclass', "Alle")
    form2.process()
    allItems = item()
    dinge = allItems.filter(session.get('filter',{}))
    tabel = ItemTable(dinge)
    return render_template('index.html', title='Home', form=form, form2=form2, tabel=tabel)

@app.route('/update/<id>/<richtung>', methods=['POST'])
def update(id,richtung):
    updateItem = item()
    if richtung == "True":
        updateItem.update(id, False)
    else:
        updateItem.update(id, True)
    flash("Item " + id + " wurde geändert! " + richtung)
    return redirect('/index')